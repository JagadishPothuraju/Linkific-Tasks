from pathlib import Path
import uuid, os, shutil
from typing import List
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

ROOT=Path(__file__).resolve().parent
UPLOADS=ROOT/"uploads"; UPLOADS.mkdir(exist_ok=True)
CHROMA_DB=ROOT/"chroma_db"; CHROMA_DB.mkdir(exist_ok=True)
MAX_BYTES=int(os.getenv("MAX_FILE_BYTES",10*1024*1024))
ALLOWED={".pdf",".txt"}
CHUNK_SIZE=int(os.getenv("CHUNK_SIZE",700))
OVERLAP=int(os.getenv("CHUNK_OVERLAP",100))
app=FastAPI(title="Day 17 Complete RAG API",version="1.0.0")
model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def init_chroma():
    db_path=str(CHROMA_DB)
    try:
        client=chromadb.PersistentClient(path=db_path)
        client.get_or_create_collection("company_docs",metadata={"hnsw:space":"cosine"})
        return client
    except Exception as exc:
        print(f"ChromaDB init failed, resetting local database: {exc}")
        shutil.rmtree(CHROMA_DB, ignore_errors=True)
        CHROMA_DB.mkdir(exist_ok=True)
        client=chromadb.PersistentClient(path=db_path)
        return client

client=init_chroma()
collection=client.get_or_create_collection("company_docs",metadata={"hnsw:space":"cosine"})

class Question(BaseModel):
    question:str=Field(...,min_length=3,max_length=1000)
    top_k:int=Field(default=4,ge=1,le=10)

def read_doc(path,suffix):
    if suffix==".txt": return path.read_text(encoding="utf-8",errors="replace")
    reader=PdfReader(str(path))
    return "\\n".join((p.extract_text() or "") for p in reader.pages)

def chunks_for(text):
    splitter=RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=min(OVERLAP,CHUNK_SIZE-1),separators=["\\n\\n","\\n",". "," ",""])
    return splitter.split_text(text)

@app.get("/")
def home():
    return {"message":"RAG API is running","docs":"/docs","endpoints":["/upload","/ask","/health"]}

@app.get("/health")
def health():
    return {"status":"ok","indexed_chunks":collection.count()}

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    name=Path(file.filename or "").name
    suffix=Path(name).suffix.lower()
    if not name: raise HTTPException(400,"Filename is required.")
    if suffix not in ALLOWED: raise HTTPException(415,"Unsupported file type. Upload PDF or TXT.")
    doc_id=str(uuid.uuid4()); path=UPLOADS/(doc_id+suffix); size=0
    try:
        with path.open("wb") as out:
            while True:
                block=await file.read(1024*1024)
                if not block: break
                size+=len(block)
                if size>MAX_BYTES:
                    path.unlink(missing_ok=True)
                    raise HTTPException(413,f"File exceeds upload limit of {MAX_BYTES//(1024*1024)} MB.")
                out.write(block)
        if size==0:
            path.unlink(missing_ok=True)
            raise HTTPException(400,"Uploaded file is empty.")
        try: text=read_doc(path,suffix)
        except Exception as exc:
            path.unlink(missing_ok=True)
            raise HTTPException(400,"Could not read document; it may be corrupted.") from exc
        if not text.strip():
            path.unlink(missing_ok=True)
            raise HTTPException(422,"No extractable text found. Scanned PDFs may require OCR.")
        chunks=chunks_for(text)
        if not chunks: raise HTTPException(422,"Document produced no text chunks.")
        vectors=model.encode(chunks,normalize_embeddings=True).tolist()
        ids=[f"{doc_id}_{i}" for i in range(len(chunks))]
        metas=[{"document_id":doc_id,"filename":name,"chunk_index":i,"source_type":suffix[1:]} for i in range(len(chunks))]
        collection.add(ids=ids,documents=chunks,embeddings=vectors,metadatas=metas)
        return {"message":"Document indexed successfully","document_id":doc_id,"filename":name,"file_size_bytes":size,"chunks_created":len(chunks),"chunk_size":CHUNK_SIZE}
    finally:
        await file.close()

@app.post("/ask")
def ask(req:Question):
    count=collection.count()
    if count==0: raise HTTPException(409,"No documents indexed. Upload a PDF or TXT first.")
    qvec=model.encode([req.question],normalize_embeddings=True).tolist()
    result=collection.query(query_embeddings=qvec,n_results=min(req.top_k,count))
    docs=result["documents"][0]; metas=result["metadatas"][0]; distances=result["distances"][0]
    if not docs: raise HTTPException(404,"No relevant passages found.")
    sources=[{"filename":m.get("filename"),"chunk_index":m.get("chunk_index"),"similarity_estimate":round(1-float(d),4),"excerpt":t[:350]} for t,m,d in zip(docs,metas,distances)]
    return {"answer":"\\n\\n".join(docs),"sources":sources,"note":"Starter version returns retrieved passages. Connect an LLM to generate fluent answers, and verify responses against source documents."}
