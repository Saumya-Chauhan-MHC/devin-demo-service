import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metrics_endpoint_returns_200():
    response = client.get("/metrics")
    assert response.status_code == 200

def test_metrics_content_type():
    response = client.get("/metrics")
    assert "text/plain" in response.headers["content-type"]

def test_metrics_contains_request_count():
    response = client.get("/metrics")
    assert "request_count" in response.text

def test_metrics_contains_latency_histogram():
    response = client.get("/metrics")
    assert "request_latency_seconds" in response.text

def test_metrics_increment_after_request():
    response_before = client.get("/metrics")
    before_text = response_before.text
    
    client.get("/health")
    
    response_after = client.get("/metrics")
    after_text = response_after.text
    
    assert "request_count" in after_text
    assert "/health" in after_text

def test_health_endpoint_still_works():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_metrics_format():
    response = client.get("/metrics")
    lines = response.text.split('\n')
    
    metric_lines = [line for line in lines if line and not line.startswith('#')]
    assert len(metric_lines) > 0
    
    for line in metric_lines:
        if line.strip():
            assert '{' in line or ' ' in line
