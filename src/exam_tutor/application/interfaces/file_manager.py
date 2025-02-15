from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import (
    AnswerVideoLink,
    TaskFileLink,
    TaskPhotoLink,
    TaskSoundLink,
)


class FileManager(Protocol):
    @abstractmethod
    async def save_answer_video(
        self, payload: bytes, answer_video_link: AnswerVideoLink, content_type: str
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

    @abstractmethod
    async def get_answer_video_public_url(
        self, answer_video_link: AnswerVideoLink
    ) -> str: ...

    @abstractmethod
    async def get_task_sound_file_public_url(
        self,
        task_sound_file_link: TaskSoundLink,
    ) -> str: ...

    @abstractmethod
    async def get_task_file_file_public_url(
        self,
        task_file_file_link: TaskFileLink,
    ) -> str: ...

    @abstractmethod
    async def get_task_photo_file_public_url(
        self,
        task_photo_file_link: TaskPhotoLink,
    ) -> str: ...
