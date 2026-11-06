# Day 28 — Improved AI Resume Screening System

## Contents
- `app.py`: Streamlit interface.
- `src/resume_analyzer.py`: modular analysis, upload validation and extraction.
- `tests/`: unit tests.
- `docs/CODE_REVIEW_REPORT.md`: review findings.
- `GIT_COMMIT.txt` and `git_changes.patch`: Git change record.
- `sample_data/`: synthetic test inputs.

## Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
Open the local URL printed by Streamlit, usually http://localhost:8501.

## Tests
```powershell
python -m pytest -q
```

## Git commit
After extraction, run:
```powershell
git init
git add .
git commit -m "Improve resume analysis validation and code quality"
```

Use synthetic resumes only. This educational tool must not automatically rank, select or reject applicants.
