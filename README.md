# devin-demo-service

A demo FastAPI service with structured JSON logging and request_id propagation.

## Features

- **Structured JSON Logging**: All logs are output in JSON format for easy parsing
- **Request ID Propagation**: Each request gets a unique request_id that appears in all related log entries
- **Configurable Log Level**: Set log level via `LOG_LEVEL` environment variable

## Request ID Propagation

The service automatically generates a unique `request_id` (UUID4) for each incoming HTTP request. If the client sends an `X-Request-ID` header, that value is used instead, enabling request tracing across multiple services.

The `request_id` is:
- Included in all log entries during request processing
- Returned in the response via the `X-Request-ID` header

## Configuration

### Log Level

Set the log level using the `LOG_LEVEL` environment variable:

```bash
export LOG_LEVEL=DEBUG
# Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
# Default: INFO
```

## Log Format

Logs are output as JSON with the following structure:

```json
{
  "timestamp": "2024-10-04T00:12:15.123456Z",
  "level": "INFO",
  "message": "Log message here",
  "logger": "app.main",
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

## Filtering Logs with jq

Use `jq` to filter and analyze logs by request_id:

### Filter logs by specific request_id
```bash
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000")'
```

### Show only messages for a specific request_id
```bash
cat logs.json | jq -r 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000") | .message'
```

### Group and count logs by request_id
```bash
cat logs.json | jq -r '.request_id' | sort | uniq -c | sort -rn
```

### Show logs for a specific request_id with timestamp and level
```bash
cat logs.json | jq -r 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000") | "\(.timestamp) [\(.level)] \(.message)"'
```

### Filter by request_id and log level
```bash
cat logs.json | jq 'select(.request_id == "550e8400-e29b-41d4-a716-446655440000" and .level == "ERROR")'
```

## Running the Service

```bash
uvicorn app.main:app --reload
```
