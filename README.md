# devin-demo-service

A minimal FastAPI service with Prometheus metrics support.

## Features

- `/health` - Health check endpoint
- `/metrics` - Prometheus metrics endpoint

## Metrics

The service exports the following Prometheus metrics:

- `request_count{method,path,status}` - Total number of HTTP requests
- `request_latency_seconds{method,path}` - HTTP request latency histogram

## Prometheus Configuration

Add the following to your `prometheus.yml` to scrape metrics from this service:

```yaml
scrape_configs:
  - job_name: 'devin-demo-service'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'
    scrape_interval: 15s
```

## Running the Service

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Running Tests

```bash
pytest
```
