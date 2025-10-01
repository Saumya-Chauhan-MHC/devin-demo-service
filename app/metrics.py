# TODO: implement Prometheus /metrics exporter
def render_metrics_text() -> str:
    """
    Return Prometheus text-format metrics.
    Example:
      request_count{path="/health",method="GET",status="200"} 42
    """
    raise NotImplementedError("Metrics exporter not implemented yet")
