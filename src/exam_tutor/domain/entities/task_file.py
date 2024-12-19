from dataclasses import dataclass
from typing import NewType
from uuid import UUID

TaskFileId = NewType('TaskFileId', UUID)
TaskFileLink = NewType('TaskFileLink', str)


@dataclass(slots=True)
class TaskFile:
    id: TaskFileId
    link: TaskFileLink
