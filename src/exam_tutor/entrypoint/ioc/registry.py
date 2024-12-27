from typing import Iterable

from dishka import Provider

from exam_tutor.entrypoint.ioc.adapters import SqlaProvider
from exam_tutor.entrypoint.ioc.interactors import InteractorProvider


def get_providers() -> Iterable[Provider]:
    return (
        SqlaProvider(),
        InteractorProvider(),
    )
