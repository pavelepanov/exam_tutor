from dishka import AsyncContainer, Provider
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from exam_tutor.controllers.http.base.root_router import root_router
from exam_tutor.entrypoint.ioc.registry import get_providers
from exam_tutor.entrypoint.setup import (
    configure_app,
    create_app,
    create_async_ioc_container,
)


def make_app(*di_providers: Provider) -> FastAPI:
    app = create_app()
    configure_app(app=app, root_router=root_router)

    async_ioc_container: AsyncContainer = create_async_ioc_container(
        providers=(*get_providers(), *di_providers)
    )

    setup_dishka(container=async_ioc_container, app=app)

    return app
