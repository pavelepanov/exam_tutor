from dataclasses import dataclass
from typing import NewType
from uuid import UUID

AnswerVideoId = NewType("VideoId", UUID)
AnswerVideoLink = NewType("VideoLink", str)


@dataclass(slots=True)
class AnswerVideo:
    id: AnswerVideoId
    link: AnswerVideoLink
