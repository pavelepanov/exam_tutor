from logging import DEBUG, FileHandler, StreamHandler, basicConfig
from typing import Iterable

from dishka import AsyncContainer, Provider, make_async_container
from fastapi import APIRouter, FastAPI

from exam_tutor.controllers.http.base.error_handler import init_error_handlers
from exam_tutor.entrypoint.config import Config, MinIOConfig, PostgresConfig, S3Buckets


def create_app() -> FastAPI:
    app = FastAPI()

    return app


def create_async_ioc_container(providers: Iterable[Provider]) -> AsyncContainer:
    config = Config(
        minio_config=MinIOConfig.from_env(),
        postgres_config=PostgresConfig.from_env(),
        s3_buckets=S3Buckets.from_env(),
    )
    return make_async_container(
        *providers,
        context={Config: config},
    )


def configure_app(app: FastAPI, root_router: APIRouter) -> None:
    app.include_router(root_router)
    init_error_handlers(app)


def configure_logging(level=DEBUG):
    format = "[%(asctime)s.%(msecs)03d] %(module)15s:%(lineno)-3d %(levelname)-7s \
     - %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    file_handler = FileHandler("logs.log")
    file_handler.setLevel(level)

    stream_handler = StreamHandler()
    stream_handler.setLevel(level)

    basicConfig(
        level=level,
        datefmt=datefmt,
        format=format,
        handlers=[file_handler, stream_handler],
    )
