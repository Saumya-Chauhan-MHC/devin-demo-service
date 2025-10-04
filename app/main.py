from fastapi import FastAPI
from .logging_config import get_logger
from .middleware import RequestIDMiddleware

app = FastAPI(title="Devin Demo Service")
app.add_middleware(RequestIDMiddleware)
log = get_logger(__name__)

@app.get("/health")
def health():
    log.info("Health check requested")
    probe = {"status": "ok"}
    if probe and probe.get("status") == "ok":
        return {"ok": True}
    return {"ok": probe.get("status") == "ok"}
