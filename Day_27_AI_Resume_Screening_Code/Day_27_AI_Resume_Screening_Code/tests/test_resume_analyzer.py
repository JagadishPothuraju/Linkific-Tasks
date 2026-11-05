from src.resume_analyzer import find_skills, analyze_resume


def test_find_skills_is_case_insensitive():
    assert "python" in find_skills("I use PYTHON and SQL.")


def test_find_skills_avoids_partial_word_match():
    assert "java" not in find_skills("I enjoy javascript development.", ["java"])


def test_analyze_resume_reports_matches_and_missing_skills():
    resume = "Python developer with SQL and pandas experience."
    job = "Need Python, SQL, machine learning and Docker."
    result = analyze_resume(resume, job)
    assert result["matched_skills"] == ["python", "sql"]
    assert result["missing_skills"] == ["docker", "machine learning"]
    assert 0 <= result["similarity_score"] <= 100
