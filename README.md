# devin-demo-service

A FastAPI service with structured JSON logging and request_id propagation.

## Features

- Structured JSON logging
- Request ID propagation across all log entries
- Configurable log levels via environment variable
- Compatible with distributed tracing via X-Request-ID headers

## Logging

This service uses structured JSON logging with request_id propagation for better observability and tracing.

### Request ID

Each HTTP request is automatically assigned a unique `request_id` (UUID4 format). If the client sends an `X-Request-ID` header, that value is used instead to enable distributed tracing across services. The request_id is included in:

- All log entries generated during the request processing
- The response headers as `X-Request-ID`

### Log Level Configuration

Configure the log level via the `LOG_LEVEL` environment variable:

```bash
LOG_LEVEL=DEBUG uvicorn app.main:app
```

Supported levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` (default: `INFO`)

### Log Format

Logs are output in JSON format with the following fields:

```json
{
  "timestamp": "2025-10-04T00:15:00.123456Z",
  "level": "INFO",
  "message": "Log message here",
  "logger": "app.main",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### Filtering Logs with jq

Use `jq` to filter and analyze JSON logs:

```bash
# Filter logs for a specific request_id
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000")'

# Show only ERROR level logs for a specific request
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000" and .level == "ERROR")'

# Get all logs for a request, sorted by timestamp
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000")' | jq -s 'sort_by(.timestamp)'

# Count log entries per request_id
cat logs.json | jq -s 'group_by(.request_id) | map({request_id: .[0].request_id, count: length})'

# Extract all unique request_ids
cat logs.json | jq -r '.request_id' | sort -u

# Show all WARNING and ERROR logs
cat logs.json | jq 'select(.level == "WARNING" or .level == "ERROR")'
```

## Running the Service

```bash
# Standard mode
uvicorn app.main:app --reload

# With debug logging
LOG_LEVEL=DEBUG uvicorn app.main:app --reload

# With custom host and port
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## API Endpoints

- `GET /health` - Health check endpoint
