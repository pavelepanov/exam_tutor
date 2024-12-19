from dataclasses import dataclass
from typing import NewType
from uuid import UUID

TaskPhotoId = NewType("TaskPhotoId", UUID)
TaskPhotoLink = NewType("TaskLink", str)


@dataclass(slots=True)
class TaskPhoto:
    id: TaskPhotoId
    link: TaskPhotoLink
