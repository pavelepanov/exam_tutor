from dishka import AsyncContainer, Provider
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from exam_tutor.controllers.http.base.root_router import root_router
from exam_tutor.controllers.http.middlewares.registry import setup_middlewares
from exam_tutor.entrypoint.ioc.registry import get_providers
from exam_tutor.entrypoint.setup import (
    configure_app,
    configure_logging,
    create_app,
    create_async_ioc_container,
)
from exam_tutor.infrastructure.sqla_persistence.mappings.map import map_tables


def make_app(*di_providers: Provider) -> FastAPI:
    app = create_app()
    map_tables()
    configure_app(app=app, root_router=root_router)

    async_ioc_container: AsyncContainer = create_async_ioc_container(
        providers=(*get_providers(), *di_providers)
    )

    setup_dishka(container=async_ioc_container, app=app)
    setup_middlewares(app=app)

    configure_logging()

    return app
