from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import TaskPhotoLink


class GenerationTaskPhotoLink(Protocol):
    @abstractmethod
    async def generate_task_photo_link(self) -> TaskPhotoLink: ...
