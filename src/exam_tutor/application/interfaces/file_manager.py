from abc import abstractmethod
from typing import Protocol


class FileManager(Protocol):
    @abstractmethod
    async def save_answer_video(
        self, payload: bytes, answer_video_link: str, content_type: str
    ) -> None: ...
