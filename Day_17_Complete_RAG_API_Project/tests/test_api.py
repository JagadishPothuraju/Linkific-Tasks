from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_unsupported_extension():
    r = client.post("/upload", files={"file": ("bad.docx", b"demo", "application/octet-stream")})
    assert r.status_code == 415

def test_empty_file():
    r = client.post("/upload", files={"file": ("empty.txt", b"", "text/plain")})
    assert r.status_code == 400

def test_question_validation():
    r = client.post("/ask", json={"question": "a"})
    assert r.status_code == 422
