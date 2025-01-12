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
    task_sound_links: list[TaskSoundLink] | None
    task_file_links: list[TaskFileLink] | None
    task_photo_links: list[TaskPhotoLink] | None
    answer_video_link: AnswerVideoLink | None
