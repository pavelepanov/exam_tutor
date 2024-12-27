from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import Task, TaskId, FindCode


class TaskDataGateway(Protocol):
    @abstractmethod
    def read_by_find_code(self, find_code: FindCode) -> Task | None: ...
