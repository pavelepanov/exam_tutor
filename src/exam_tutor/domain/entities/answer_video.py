from dataclasses import dataclass
from uuid import UUID
from typing import NewType


AnswerVideoId = NewType('VideoId', UUID)
AnswerVideoLink = NewType('VideoLink', str)


@dataclass(slots=True)
class AnswerVideo:
    id: AnswerVideoId
    link: AnswerVideoLink
