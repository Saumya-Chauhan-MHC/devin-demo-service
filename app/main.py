import time
from fastapi import FastAPI, Request, Response
from .logging_config import get_logger
from .metrics import render_metrics_text, get_content_type, request_count, request_latency_seconds

app = FastAPI(title="Devin Demo Service")
log = get_logger(__name__)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    path = request.url.path
    method = request.method
    status = str(response.status_code)
    
    request_count.labels(method=method, path=path, status=status).inc()
    request_latency_seconds.labels(method=method, path=path).observe(duration)
    
    return response

@app.get("/health")
def health():
    probe = {"status": "ok"}  # pretend this is flaky in staging
    if probe and probe.get("status") == "ok":
        return {"ok": True}
    return {"ok": probe.get("status") == "ok"}  # will crash if probe=None (useful for a bug issue)

@app.get("/metrics")
def metrics():
    return Response(content=render_metrics_text(), media_type=get_content_type())
