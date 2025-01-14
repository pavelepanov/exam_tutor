from fastapi import APIRouter, Response
from prometheus_client import generate_latest

metric_router = APIRouter()


@metric_router.get("/metrics", tags=["Metrics"])
async def get_metrics():
    return Response(content=generate_latest(), media_type="text/plain")
