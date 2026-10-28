import pytest
from fastapi.testclient import TestClient

from app import config
from app.main import app

config.DB_LATENCY = 0.05
config.EMAIL_LATENCY = 0.3

client = TestClient(app)
ORDER = {"customer_email": "a@b.com", "item": "book", "quantity": 2}


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


@pytest.mark.parametrize("v", ["v1", "v2"])
def test_get_user(v):
    r = client.get(f"/api/{v}/users/7")
    assert r.status_code == 200 and r.json()["id"] == 7


def test_middleware_header():
    assert "x-process-time-ms" in client.get("/api/v2/users/1").headers


@pytest.mark.parametrize("bad", [
    {**ORDER, "quantity": 0},
    {**ORDER, "quantity": 101},
    {**ORDER, "item": ""},
    {**ORDER, "customer_email": "nope"},
])
def test_validation_422(bad):
    assert client.post("/api/v2/orders", json=bad).status_code == 422


def test_v2_order_faster_than_v1():
    r1 = client.post("/api/v1/orders", json=ORDER)
    r2 = client.post("/api/v2/orders", json=ORDER)
    assert r1.status_code == r2.status_code == 200
    assert r1.json() == r2.json()
    d1 = float(r1.headers["x-process-time-ms"])
    d2 = float(r2.headers["x-process-time-ms"])
    assert d1 > d2


def test_fan_out():
    r = client.get("/api/v2/users", params={"ids": "1,2,3"})
    assert [u["id"] for u in r.json()] == [1, 2, 3]
