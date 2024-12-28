from abc import abstractmethod
from datetime import datetime
from typing import Protocol

from exam_tutor.domain.entities.task import (
    AnswerVideoLink,
    Condition,
    DifficultEnum,
    ExamEnum,
    ExamTaskNumber,
    FindCode,
    StrAnswer,
    SubjectEnum,
    Task,
    TaskFileLink,
    TaskId,
    TaskPhotoLink,
    TaskSoundLink,
)


class TaskDataGateway(Protocol):
    @abstractmethod
    async def read_by_find_code(self, find_code: FindCode) -> Task | None: ...

    @abstractmethod
    async def create_task(
        self,
        id: TaskId,
        exam: ExamEnum,
        subject: SubjectEnum,
        exam_task_number: ExamTaskNumber,
        condition: Condition,
        answer: StrAnswer,
        difficult: DifficultEnum,
        created_at: datetime,
        find_code: FindCode,
        task_sound_link: TaskSoundLink | None = None,
        task_file_link: TaskFileLink | None = None,
        task_photo_link: TaskPhotoLink | None = None,
        answer_video_link: AnswerVideoLink | None = None,
    ) -> Task: ...
