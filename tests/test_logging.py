import pytest
import json
from fastapi.testclient import TestClient
from app.main import app
from app.logging_config import get_logger, JsonFormatter
from app.middleware import request_id_context

client = TestClient(app)

def test_log_includes_request_id(caplog):
    request_id_context.set("test-request-456")
    logger = get_logger("test_logger")
    
    with caplog.at_level("INFO"):
        logger.info("Test message")
    
    formatter = JsonFormatter()
    formatted = formatter.format(caplog.records[0])
    log_data = json.loads(formatted)
    
    assert log_data["request_id"] == "test-request-456"
    assert log_data["message"] == "Test message"

def test_log_without_request_id(caplog):
    request_id_context.set(None)
    logger = get_logger("test_logger_no_id")
    
    with caplog.at_level("INFO"):
        logger.info("Test message without request_id")
    
    formatter = JsonFormatter()
    formatted = formatter.format(caplog.records[0])
    log_data = json.loads(formatted)
    
    assert "request_id" not in log_data
    assert log_data["message"] == "Test message without request_id"

def test_log_level_env_override(monkeypatch):
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    logger = get_logger("test_env_logger")
    assert logger.level == 10

    monkeypatch.setenv("LOG_LEVEL", "ERROR")
    logger2 = get_logger("test_env_logger2")
    assert logger2.level == 40
