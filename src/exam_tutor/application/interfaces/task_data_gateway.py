from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import Task, TaskId


class TaskDataGateway(Protocol):
    @abstractmethod
    def read_by_uuid(self, id: TaskId) -> Task | None: ...
