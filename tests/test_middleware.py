import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_middleware_generates_request_id():
    response = client.get("/health")
    assert response.status_code == 200
    assert "X-Request-ID" in response.headers
    assert len(response.headers["X-Request-ID"]) > 0

def test_middleware_preserves_incoming_request_id():
    test_request_id = "test-request-123"
    response = client.get("/health", headers={"X-Request-ID": test_request_id})
    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == test_request_id

def test_request_id_in_different_requests():
    response1 = client.get("/health")
    response2 = client.get("/health")
    assert response1.headers["X-Request-ID"] != response2.headers["X-Request-ID"]
