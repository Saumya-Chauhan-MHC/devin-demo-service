from fastapi import FastAPI
from .logging_config import get_logger
from .middleware import RequestIdMiddleware

app = FastAPI(title="Devin Demo Service")
app.add_middleware(RequestIdMiddleware)
log = get_logger(__name__)

@app.get("/health")
def health():
    log.info("Health check endpoint called")
    probe = {"status": "ok"}  # pretend this is flaky in staging
    if probe and probe.get("status") == "ok":
        return {"ok": True}
    return {"ok": probe.get("status") == "ok"}  # will crash if probe=None (useful for a bug issue)
