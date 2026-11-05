"""Simple, explainable resume-to-job-description analysis for learning purposes."""

from pathlib import Path
import re

SKILL_TERMS = [
    "python", "java", "javascript", "sql", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "streamlit", "flask", "fastapi", "react", "html", "css", "git", "docker",
    "communication", "project management", "natural language processing", "nlp"
]


def extract_text_from_file(uploaded_file):
    """Extract text from an uploaded TXT, PDF or DOCX file-like object."""
    filename = getattr(uploaded_file, "name", "resume.txt").lower()
    content = uploaded_file.read()
    if filename.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")
    if filename.endswith(".pdf"):
        try:
            import fitz
        except ImportError as exc:
            raise RuntimeError("Install PyMuPDF with: python -m pip install PyMuPDF") from exc
        chunks = []
        with fitz.open(stream=content, filetype="pdf") as pdf:
            for page in pdf:
                chunks.append(page.get_text())
        return "\n".join(chunks)
    if filename.endswith(".docx"):
        try:
            from docx import Document
            import io
        except ImportError as exc:
            raise RuntimeError("Install python-docx with: python -m pip install python-docx") from exc
        document = Document(io.BytesIO(content))
        return "\n".join(p.text for p in document.paragraphs)
    raise ValueError("Unsupported file type. Upload PDF, DOCX or TXT.")


def find_skills(text, skill_terms=None):
    """Return configured skills found as whole phrases, case-insensitively."""
    terms = skill_terms or SKILL_TERMS
    normalized = text.lower()
    found = []
    for term in terms:
        pattern = r"(?<![a-z0-9+#.])" + re.escape(term.lower()) + r"(?![a-z0-9+#.])"
        if re.search(pattern, normalized):
            found.append(term)
    return sorted(set(found))


def calculate_similarity(resume_text, job_description):
    """Return TF-IDF cosine similarity as a percentage; zero for empty input."""
    if not resume_text.strip() or not job_description.strip():
        return 0.0
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError as exc:
        raise RuntimeError("Install dependencies with: python -m pip install -r requirements.txt") from exc
    matrix = TfidfVectorizer(stop_words="english").fit_transform([resume_text, job_description])
    return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100, 1)


def analyze_resume(resume_text, job_description):
    """Create a basic match summary. This is not a hiring recommendation."""
    job_skills = find_skills(job_description)
    resume_skills = find_skills(resume_text)
    matched = sorted(set(job_skills).intersection(resume_skills))
    missing = sorted(set(job_skills).difference(resume_skills))
    return {
        "similarity_score": calculate_similarity(resume_text, job_description),
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
    }
