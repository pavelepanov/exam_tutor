from dishka import Provider, Scope, provide

from exam_tutor.application.interactors.create_task import CreateTaskInteractor
from exam_tutor.application.interactors.get_task_by_find_code import (
    GetTaskByFindCodeInteractor,
)


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    get_task_by_find_code = provide(GetTaskByFindCodeInteractor)
    create_task = provide(CreateTaskInteractor)
