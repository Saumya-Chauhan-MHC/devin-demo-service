from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_returns_200():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_endpoint_returns_ok_true():
    response = client.get("/health")
    assert response.json() == {"ok": True}

def test_probe_none_logic():
    probe = None
    result = probe.get("status") == "ok" if probe else False
    assert result == False

def test_probe_ok_logic():
    probe = {"status": "ok"}
    result = probe.get("status") == "ok" if probe else False
    assert result == True

def test_probe_not_ok_logic():
    probe = {"status": "error"}
    result = probe.get("status") == "ok" if probe else False
    assert result == False
