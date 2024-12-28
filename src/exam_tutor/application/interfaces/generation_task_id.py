from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import TaskId


class GenerationTaskId(Protocol):
    @abstractmethod
    async def generate_task_id(self) -> TaskId: ...
