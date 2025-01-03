from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import TaskSoundLink


class GenerationTaskSoundLink(Protocol):
    @abstractmethod
    async def generate_task_sound_link(self) -> TaskSoundLink: ...
