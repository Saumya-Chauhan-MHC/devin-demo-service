from fastapi import FastAPI
from .logging_config import get_logger

app = FastAPI(title="Devin Demo Service")
log = get_logger(__name__)

@app.get("/health")
def health():
    probe = {"status": "ok"}  # pretend this is flaky in staging
    if probe and probe.get("status") == "ok":
        return {"ok": True}
    return {"ok": probe.get("status") == "ok"}  # will crash if probe=None (useful for a bug issue)
