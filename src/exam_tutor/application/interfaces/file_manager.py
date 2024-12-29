from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import TaskId


class FileManager(Protocol):
    @abstractmethod
    async def save(self, payload: bytes, path: str) -> None: ...

    @abstractmethod
    async def get_by_file_link(self, file_path: str) -> bytes | None: ...


def create_file_path(task_id: TaskId, extension: str) -> str:
    return f"{task_id}.{extension}"
