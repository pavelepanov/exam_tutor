from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from exam_tutor.domain.entities.answer_video import AnswerVideoId
from exam_tutor.domain.entities.task_file import TaskFileId
from exam_tutor.domain.entities.task_photo import TaskPhotoId
from exam_tutor.domain.entities.task_sound import TaskSoundId
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
    task_sound_id: TaskSoundId | None
    task_file_id: TaskFileId | None
    task_photo_id: TaskPhotoId | None
    answer_video_id: AnswerVideoId | None
    created_at: datetime
