import io
import pytest
from src.resume_analyzer import find_skills, analyze_resume, extract_text_from_file, ResumeProcessingError

def test_case_insensitive_skills():
    assert find_skills("PYTHON and SQL") == ["python","sql"]

def test_no_partial_word_match():
    assert "java" not in find_skills("javascript",["java"])

def test_matches_and_missing():
    result=analyze_resume("Python developer with SQL and pandas","Need Python, SQL, machine learning and Docker")
    assert result["matched_skills"] == ["python","sql"]
    assert result["missing_skills"] == ["docker","machine learning"]
    assert 0 <= result["similarity_score"] <= 100

def test_empty_resume():
    with pytest.raises(ValueError,match="Resume text is empty"): analyze_resume(" ","Need Python")

def test_empty_job_description():
    with pytest.raises(ValueError,match="Job description is empty"): analyze_resume("Python"," ")

def test_unsupported_file():
    with pytest.raises(ResumeProcessingError,match="Unsupported"): extract_text_from_file(io.BytesIO(b"x"),"resume.exe")

def test_empty_upload():
    with pytest.raises(ResumeProcessingError,match="empty"): extract_text_from_file(io.BytesIO(b""),"resume.txt")

def test_txt_extraction():
    assert extract_text_from_file(io.BytesIO(b"Python developer"),"resume.txt")=="Python developer"
