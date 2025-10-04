import uuid
from fastapi import FastAPI
from .logging_config import get_logger, request_id_var

app = FastAPI(title="Devin Demo Service")
log = get_logger(__name__)

@app.middleware("http")
async def request_id_middleware(request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request_id_var.set(request_id)
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

@app.get("/health")
def health():
    probe = {"status": "ok"}  # pretend this is flaky in staging
    if probe and probe.get("status") == "ok":
        return {"ok": True}
    return {"ok": probe.get("status") == "ok"}  # will crash if probe=None (useful for a bug issue)
