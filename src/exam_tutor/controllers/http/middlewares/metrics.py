from fastapi import Request
from prometheus_client import Counter
from starlette.middleware.base import BaseHTTPMiddleware

REQUEST_COUNT = Counter(
    "http_requests_total", "Total number of HTTP requests", ["method", "endpoint"]
)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
        return response
