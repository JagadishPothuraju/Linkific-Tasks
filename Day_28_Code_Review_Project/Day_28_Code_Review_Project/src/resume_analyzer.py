"""Modular resume parsing and comparison helpers."""
import re

SKILLS=("python","java","javascript","sql","machine learning","deep learning","data analysis","pandas","numpy","scikit-learn","tensorflow","pytorch","streamlit","flask","fastapi","react","html","css","git","docker","communication","project management","nlp","natural language processing")

class ResumeProcessingError(ValueError):
    """Raised when an uploaded resume cannot be processed safely."""

def extract_text_from_file(uploaded_file, filename, max_bytes=5*1024*1024):
    """Validate and extract text from TXT, PDF or DOCX files."""
    ext=filename.lower().rsplit(".",1)[-1] if "." in filename else ""
    if ext not in {"txt","pdf","docx"}:
        raise ResumeProcessingError("Unsupported file type. Upload PDF, DOCX or TXT.")
    data=uploaded_file.read(max_bytes+1)
    if not data: raise ResumeProcessingError("The uploaded file is empty.")
    if len(data)>max_bytes: raise ResumeProcessingError("File exceeds the 5 MB limit.")
    if ext=="txt": return data.decode("utf-8",errors="replace").strip()
    if ext=="pdf":
        try:
            import fitz
            with fitz.open(stream=data,filetype="pdf") as pdf:
                return "\\n".join(page.get_text() for page in pdf).strip()
        except ImportError as exc: raise ResumeProcessingError("Install PDF support: python -m pip install PyMuPDF") from exc
        except Exception as exc: raise ResumeProcessingError("Invalid or unreadable PDF file.") from exc
    try:
        from docx import Document
        import io
        return "\\n".join(p.text for p in Document(io.BytesIO(data)).paragraphs).strip()
    except ImportError as exc: raise ResumeProcessingError("Install DOCX support: python -m pip install python-docx") from exc
    except Exception as exc: raise ResumeProcessingError("Invalid or unreadable DOCX file.") from exc

def find_skills(text, terms=SKILLS):
    """Find configured skill phrases without partial-word matches."""
    if not isinstance(text,str): raise TypeError("Text must be a string.")
    found=[]
    for term in terms:
        term=term.strip().lower()
        if term and re.search(r"(?<![a-z0-9+#.])"+re.escape(term)+r"(?![a-z0-9+#.])",text.lower()):
            found.append(term)
    return sorted(set(found))

def calculate_similarity(resume_text, job_description):
    """Calculate TF-IDF cosine similarity as a percentage."""
    if not resume_text.strip() or not job_description.strip(): return 0.0
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        matrix=TfidfVectorizer(stop_words="english").fit_transform([resume_text,job_description])
        return round(max(0.0,min(100.0,float(cosine_similarity(matrix[0:1],matrix[1:2])[0][0])*100)),1)
    except ImportError as exc: raise RuntimeError("Install dependencies using python -m pip install -r requirements.txt") from exc
    except ValueError: return 0.0

def analyze_resume(resume_text, job_description):
    """Return a transparent comparison; this is not a hiring recommendation."""
    if not isinstance(resume_text,str) or not isinstance(job_description,str): raise TypeError("Inputs must be text.")
    if not resume_text.strip(): raise ValueError("Resume text is empty.")
    if not job_description.strip(): raise ValueError("Job description is empty.")
    resume=find_skills(resume_text); job=find_skills(job_description)
    return {"similarity_score":calculate_similarity(resume_text,job_description),
            "resume_skills":resume,"job_skills":job,
            "matched_skills":sorted(set(resume)&set(job)),
            "missing_skills":sorted(set(job)-set(resume))}
