# AI Resume Screening System

## Project overview
An educational Streamlit prototype that compares the text of a candidate resume with a job description (JD). It extracts text from supported files, identifies configured skill keywords, and calculates a TF-IDF cosine-similarity score.

> **Responsible-use note:** This is a decision-support learning prototype, not an automated hiring decision system. Similarity is text overlap, not proof of ability or job suitability. A human must review every candidate.

## Features
- Upload a resume as PDF, DOCX, or TXT.
- Extract text from the uploaded document.
- Enter a job description.
- Identify configured skills in the resume and JD.
- Display matched and missing JD skills.
- Calculate text similarity using TF-IDF and cosine similarity.
- Validate file type, empty input, and upload size.
- Provide user-friendly error messages.

## Technology stack
- Python
- Streamlit
- scikit-learn (TF-IDF and cosine similarity)
- PyMuPDF (PDF extraction)
- python-docx (DOCX extraction)
- pytest (automated tests)

## Project structure
```text
AI-Resume-Screening-System/
├── app.py
├── requirements.txt
├── src/
│   └── resume_analyzer.py
├── tests/
│   └── test_resume_analyzer.py
├── sample_data/
│   └── junior_ai_ml_jd.txt
└── README.md
```

## Setup on Windows PowerShell
1. Open PowerShell in the project folder.
2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Start the application:
   ```powershell
   python -m streamlit run app.py
   ```
5. Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## Run tests
```powershell
python -m pytest -v
```
The test suite is provided for local execution. Do not report tests as passed until you run this command and review its output.

## Demo steps
1. Start the Streamlit app.
2. Upload a sample PDF, DOCX, or TXT resume.
3. Paste a job description such as `sample_data/junior_ai_ml_jd.txt`.
4. Click **Analyze resume**.
5. Explain matched skills, missing skills, and the similarity score.
6. Explain that the score measures text similarity only.

## Limitations
- Keyword-based skill identification may miss synonyms and context.
- TF-IDF does not understand all semantic relationships.
- Scanned PDFs may require OCR, which is not included in this prototype.
- Similarity scores should not be used to automatically accept or reject applicants.
- Resume data is personal information; use only documents you are authorized to process and do not retain them unnecessarily.

## Future improvements
- Semantic embeddings and synonym-aware skill extraction.
- Secure database and access control.
- Batch processing with recruiter review tools.
- Explainable skill evidence and configurable job profiles.
- OCR support for scanned resumes.
- Bias and fairness evaluation with appropriate governance.
- Deployment with monitoring, logging, and privacy safeguards.
