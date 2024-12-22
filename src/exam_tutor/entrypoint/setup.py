from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka
from exam_tutor.entrypoint.ioc import create_container


def init_di(app: FastAPI) -> None:
    setup_dishka(create_container(), app)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)

    return app
