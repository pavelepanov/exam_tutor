from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum

TaskId = NewType("TaskId", UUID)
StrAnswer = NewType("StrAnswer", str)
Condition = NewType("Condition", str)
TaskSoundLink = NewType("TaskSoundFile", str)
TaskFileLink = NewType("TaskFileLink", str)
TaskPhotoLink = NewType("TaskPhotoLink", str)
AnswerVideoLink = NewType("AnswerVideoLink", str)
FindCode = NewType("FindCode", str)


@dataclass()
class Task:
    id: TaskId
    exam: ExamEnum
    subject: SubjectEnum
    exam_task_number: ExamTaskNumber
    condition: Condition
    answer: StrAnswer
    difficult: DifficultEnum
    created_at: datetime | None
    find_code: FindCode
    task_sound_link: TaskSoundLink | None = None
    task_file_link: TaskFileLink | None = None
    task_photo_link: TaskPhotoLink | None = None
    answer_video_link: AnswerVideoLink | None = None
