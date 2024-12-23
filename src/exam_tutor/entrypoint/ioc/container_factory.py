from dishka import AsyncContainer, Provider, Scope, make_async_container, provide
from exam_tutor.entrypoint.ioc.adapters import SqlaProvider
from exam_tutor.entrypoint.ioc.interactors import InteractorProvider


def create_async_container() -> AsyncContainer:
    return make_async_container(
        SqlaProvider(), InteractorProvider()
    )
