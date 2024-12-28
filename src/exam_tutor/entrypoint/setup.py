from typing import Iterable

from dishka import AsyncContainer, Provider, make_async_container
from fastapi import APIRouter, FastAPI
from exam_tutor.controllers.http.base.error_handler import init_error_handlers


def create_app() -> FastAPI:
    app = FastAPI()

    return app


def create_async_ioc_container(providers: Iterable[Provider]) -> AsyncContainer:
    return make_async_container(
        *providers,
    )


def configure_app(app: FastAPI, root_router: APIRouter) -> None:
    app.include_router(root_router)
    init_error_handlers(app)