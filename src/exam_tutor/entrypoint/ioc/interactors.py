from dishka import Provider, Scope, provide

from exam_tutor.application.interactors.get_task_by_find_code import GetTaskByUUIDInteractor


class InteractorProvider(Provider):
    scope = Scope.REQUEST

    get_task_by_uuid = provide(GetTaskByUUIDInteractor)