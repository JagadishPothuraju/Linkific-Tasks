# Day 17 — Complete RAG API with FastAPI

## What it does
Upload PDF/TXT files, extract text, split it into chunks, create embeddings, store chunks in ChromaDB, and retrieve relevant passages for questions.

## Run (Windows PowerShell)
```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs for Swagger UI. The embedding model downloads on first run and needs internet access.

## Test
1. Use POST `/upload` to upload `data/sample_company_handbook.txt` or an authorized PDF.
2. Use POST `/ask` with `{"question":"How many days in advance should planned leave be requested?","top_k":3}`.
3. Test empty files, unsupported extensions, corrupted PDFs, scanned PDFs, and files over 10 MB.
4. Record actual results and capture screenshots.

## Endpoints
- GET `/` — API info
- GET `/health` — service and indexed chunk count
- POST `/upload` — PDF/TXT upload
- POST `/ask` — semantic retrieval for a question

## Important
This starter version returns retrieved passages rather than inventing LLM-generated answers. Add an approved LLM provider for fluent synthesis. Do not upload confidential documents or commit API keys. Add authentication and per-user access controls before production use.
