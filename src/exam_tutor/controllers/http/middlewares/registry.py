from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from exam_tutor.controllers.http.middlewares.metrics import MetricsMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(MetricsMiddleware)
