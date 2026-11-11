import pytest
from src.resume_analyzer import (
    validate_upload, identify_skills, calculate_similarity, analyze_resume
)

def test_valid_txt_upload():
    assert validate_upload("resume.txt", 100) is True

def test_reject_unsupported_file():
    with pytest.raises(ValueError):
        validate_upload("resume.exe", 100)

def test_reject_empty_upload():
    with pytest.raises(ValueError):
        validate_upload("resume.txt", 0)

def test_identify_skills():
    assert "python" in identify_skills("Experience with Python and SQL")

def test_similarity_returns_range():
    score = calculate_similarity("Python machine learning", "Python machine learning engineer")
    assert 0.0 <= score <= 1.0

def test_empty_text_rejected():
    with pytest.raises(ValueError):
        calculate_similarity("", "Python developer")

def test_analyze_resume_finds_missing_skill():
    result = analyze_resume("Python and SQL projects", "Python, SQL and TensorFlow required")
    assert "python" in result["matched_skills"]
    assert "tensorflow" in result["missing_skills"]
