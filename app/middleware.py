import uuid
from contextvars import ContextVar
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

request_id_context: ContextVar[str] = ContextVar("request_id", default=None)

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request_id_context.set(request_id)
        
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

def get_request_id() -> str:
    return request_id_context.get()
