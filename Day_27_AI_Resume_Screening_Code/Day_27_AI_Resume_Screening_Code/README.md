# AI Resume Screening System — Day 27 Practical

A small Python + Streamlit educational prototype. It extracts text from a resume, detects configured skills, and compares the resume text with a job description using TF-IDF cosine similarity.

## Important responsible-use notice
This is a learning demonstration, not a validated recruitment product. The similarity value is not a probability of job success and must not be used to automatically rank, select or reject applicants. Do not use protected characteristics or proxies. A qualified human reviewer must verify every result. Use synthetic/sample files for testing.

## Features
- Upload PDF, DOCX or TXT resumes.
- Extract text locally.
- Detect skills from a configurable list.
- Compare resume and job description using a simple TF-IDF similarity indicator.
- Display matched and not-detected job skills.
- Includes sample data and pytest tests.

## Requirements
- Python 3.9 or newer
- Internet connection for the first dependency installation

## Windows PowerShell setup
Open PowerShell in the extracted project folder:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run this once in the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Run the app
```powershell
python -m streamlit run app.py
```
Streamlit will print a local address, usually `http://localhost:8501`. Open that address in your browser.

## Try the sample
1. Upload `sample_data/sample_resume.txt`.
2. Open `sample_data/sample_job_description.txt` in Notepad.
3. Copy its contents into the Job Description box.
4. Click **Analyze resume**.
5. Review matched skills, missing skills and similarity.

## Run tests
In the project folder:
```powershell
python -m pytest -q
```

## Customize skills
Edit `SKILL_TERMS` in `src/resume_analyzer.py`. Add only job-related skills and validate the results.

## Limitations
- The skills list is intentionally small and keyword-based.
- TF-IDF similarity measures text overlap, not competence or future job performance.
- Synonyms, context, seniority and transferable skills may be missed.
- PDF extraction may fail for scanned/image-only PDFs; OCR is not included.
- Authentication, production-grade storage, encryption, audit logging and deployment hardening are not included.
- Do not upload real candidate data unless you have authorization and appropriate privacy/security controls.
