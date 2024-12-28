from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import FindCode


class GenerationTaskFindCode(Protocol):
    @abstractmethod
    async def generate_task_find_code(self) -> FindCode: ...
