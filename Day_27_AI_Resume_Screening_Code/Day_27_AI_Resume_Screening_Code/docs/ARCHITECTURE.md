# Architecture

```text
Recruiter
   |
Streamlit UI (app.py)
   |
File text extraction (src/resume_analyzer.py)
   |
   +--> Skill keyword detection
   |
   +--> TF-IDF vectorization and cosine similarity
   |
Results: matched skills, missing skills, similarity indicator
   |
Human reviewer verifies original resume and job requirements
```

The prototype processes the uploaded file in memory and does not intentionally save resume content. It does not include a database or an automated hiring decision.
