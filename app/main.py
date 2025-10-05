from fastapi import FastAPI
from .logging_config import get_logger

app = FastAPI(title="Devin Demo Service")
log = get_logger(__name__)

@app.get("/health")
def health():
    return {"ok": True}
