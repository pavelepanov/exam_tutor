from typing import Protocol

from exam_tutor.domain.entities.task import TaskFileLink


class GenerationTaskFileLink(Protocol):
    async def generate_task_file_link(self) -> TaskFileLink: ...
