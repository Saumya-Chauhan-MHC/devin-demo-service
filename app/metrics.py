from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
from prometheus_client.exposition import CONTENT_TYPE_LATEST

request_count = Counter(
    'request_count',
    'Total HTTP requests',
    ['method', 'path', 'status']
)

request_latency_seconds = Histogram(
    'request_latency_seconds',
    'HTTP request latency in seconds',
    ['method', 'path'],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0)
)

def render_metrics_text() -> str:
    """
    Return Prometheus text-format metrics.
    Example:
      request_count{path="/health",method="GET",status="200"} 42
    """
    return generate_latest(REGISTRY).decode('utf-8')

def get_content_type() -> str:
    """Return the Prometheus metrics content type."""
    return CONTENT_TYPE_LATEST
