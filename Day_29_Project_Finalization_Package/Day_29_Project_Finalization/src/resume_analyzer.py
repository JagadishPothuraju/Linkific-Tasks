from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python", "machine learning", "deep learning", "sql", "tensorflow",
    "pytorch", "scikit-learn", "pandas", "numpy", "nlp", "generative ai",
    "git", "streamlit", "flask", "fastapi", "computer vision"
]
MAX_FILE_BYTES = 5 * 1024 * 1024

def validate_upload(filename: str, size_bytes: int):
    suffix = Path(filename).suffix.lower()
    if suffix not in {".pdf", ".docx", ".txt"}:
        raise ValueError("Unsupported file type. Upload PDF, DOCX, or TXT.")
    if size_bytes <= 0:
        raise ValueError("The uploaded file is empty.")
    if size_bytes > MAX_FILE_BYTES:
        raise ValueError("File is larger than the 5 MB limit.")
    return True

def extract_text_from_bytes(filename: str, data: bytes) -> str:
    validate_upload(filename, len(data))
    suffix = Path(filename).suffix.lower()
    if suffix == ".txt":
        text = data.decode("utf-8", errors="replace")
    elif suffix == ".pdf":
        import fitz
        text_parts = []
        with fitz.open(stream=data, filetype="pdf") as pdf:
            for page in pdf:
                text_parts.append(page.get_text())
        text = "\n".join(text_parts)
    else:
        from docx import Document
        import io
        document = Document(io.BytesIO(data))
        text = "\n".join(p.text for p in document.paragraphs)
    if not text.strip():
        raise ValueError("No readable text was found in the uploaded resume.")
    return text

def identify_skills(text: str):
    lowered = text.lower()
    return sorted(skill for skill in SKILLS if skill in lowered)

def calculate_similarity(resume_text: str, job_description: str) -> float:
    if not resume_text.strip() or not job_description.strip():
        raise ValueError("Resume text and job description must not be empty.")
    matrix = TfidfVectorizer(stop_words="english").fit_transform(
        [resume_text, job_description]
    )
    return float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])

def analyze_resume(resume_text: str, job_description: str):
    if not resume_text.strip() or not job_description.strip():
        raise ValueError("Resume text and job description must not be empty.")
    resume_skills = identify_skills(resume_text)
    jd_skills = identify_skills(job_description)
    matched = sorted(set(resume_skills) & set(jd_skills))
    missing = sorted(set(jd_skills) - set(resume_skills))
    score = calculate_similarity(resume_text, job_description)
    return {
        "similarity": score,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched,
        "missing_skills": missing,
    }
