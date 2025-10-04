# devin-demo-service

A FastAPI demo service showcasing structured JSON logging with request_id propagation.

## Features

- **Structured JSON Logging**: All logs output in JSON format with timestamp, level, message, and logger name
- **Request ID Propagation**: Each HTTP request gets a unique `request_id` that appears in all logs for that request
- **Log Level Override**: Set log level via `LOG_LEVEL` environment variable

## Request ID Propagation

The service automatically handles request IDs:
- Accepts `X-Request-ID` header from incoming requests
- Generates a UUID4 if no header is provided
- Includes `request_id` in all log entries during request processing
- Returns `X-Request-ID` in response headers for traceability

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the service:
```bash
uvicorn app.main:app --reload
```

## Configuration

Set log level via environment variable (default: INFO):
```bash
LOG_LEVEL=DEBUG uvicorn app.main:app --reload
```

Valid levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

## Testing

Run tests:
```bash
pytest tests/
```

## Filtering Logs with jq

The structured JSON logs can be easily filtered and analyzed using `jq`:

### Filter logs by specific request_id
```bash
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000")'
```

### Show only ERROR level logs
```bash
cat logs.json | jq 'select(.level == "ERROR")'
```

### Extract unique request_ids
```bash
cat logs.json | jq -r '.request_id' | sort | uniq
```

### Show all logs with errors, grouped by request_id
```bash
cat logs.json | jq 'select(.level == "ERROR") | {request_id, message, timestamp}'
```

### Count logs per request_id
```bash
cat logs.json | jq -r '.request_id' | sort | uniq -c | sort -rn
```

### Filter logs from a specific time range
```bash
cat logs.json | jq 'select(.timestamp >= "2024-01-01T00:00:00Z" and .timestamp <= "2024-01-01T23:59:59Z")'
```

## Example Log Output

```json
{"timestamp": "2024-01-15T10:30:45.123456Z", "level": "INFO", "message": "Health check requested", "logger": "app.main", "request_id": "550e8400-e29b-41d4-a716-446655440000"}
```

## API Endpoints

- `GET /health` - Health check endpoint
