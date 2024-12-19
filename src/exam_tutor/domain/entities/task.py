from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from exam_tutor.domain.entities.answer_photo import AnswerPhotoId
from exam_tutor.domain.entities.answer_video import AnswerVideoId
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum

TaskId = NewType("TaskId", UUID)
FloatAnswer = NewType("FloatAnswer", float)
StrAnswer = NewType("StrAnswer", str)
Condition = NewType("Condition", str)


@dataclass(slots=True)
class Task:
    id: TaskId
    exam: ExamEnum
    subject: SubjectEnum
    exam_task_number: ExamTaskNumber
    condition: Condition
    answer: FloatAnswer | StrAnswer
    difficult: DifficultEnum
    answer_video_id: AnswerVideoId | None
    answer_photo_id: AnswerPhotoId | None
    created_at: datetime
