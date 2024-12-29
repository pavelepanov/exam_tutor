from abc import abstractmethod
from typing import Protocol

from exam_tutor.domain.entities.task import AnswerVideoLink


class GenerationAnswerVideoLink(Protocol):
    @abstractmethod
    async def generate_answer_video_link(self) -> AnswerVideoLink: ...
