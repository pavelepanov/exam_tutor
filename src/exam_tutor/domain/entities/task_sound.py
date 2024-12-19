from dataclasses import dataclass
from typing import NewType
from uuid import UUID

TaskSoundId = NewType('TaskSoundId', UUID)
TaskSoundLink = NewType('TaskSoundLink', str)


@dataclass(slots=True)
class TaskSound:
    id: TaskSoundId
    link: TaskSoundLink
