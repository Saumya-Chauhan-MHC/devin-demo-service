from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_health_endpoint_always_returns_ok():
    for _ in range(10):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"ok": True}
