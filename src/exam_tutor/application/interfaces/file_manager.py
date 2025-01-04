from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import TaskFileLink, TaskPhotoLink, TaskSoundLink


class FileManager(Protocol):
    @abstractmethod
    async def save_answer_video(
        self, payload: bytes, answer_video_link: str, content_type: str
    ) -> None: ...

    @abstractmethod
    async def save_sound_file(
        self, file_info: dict[str, bytes | str | TaskSoundLink]
    ) -> None: ...

    @abstractmethod
    async def save_file_file(
        self, file_info: dict[str, bytes | str | TaskFileLink]
    ) -> None: ...

    @abstractmethod
    async def save_photo_file(
        self, file_info: dict[str, bytes | str | TaskPhotoLink]
    ) -> None: ...
