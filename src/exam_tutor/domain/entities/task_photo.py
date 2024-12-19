from dataclasses import dataclass
from typing import NewType
from uuid import UUID

AnswerPhotoId = NewType("AnswerPhotoId", UUID)
PhotoLink = NewType("PhotoLink", str)


@dataclass(slots=True)
class AnswerPhoto:
    id: AnswerPhotoId
    link: PhotoLink
