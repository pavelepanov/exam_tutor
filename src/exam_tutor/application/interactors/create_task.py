import logging
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from exam_tutor.application.interfaces.committer import Committer
from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.entities.task import (
    AnswerVideoLink,
    Condition,
    StrAnswer,
    Task,
    TaskFileLink,
    TaskPhotoLink,
    TaskSoundLink,
)
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum
from exam_tutor.domain.services.task import TaskService

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class CreateTaskRequest:
    exam: ExamEnum
    subject: SubjectEnum
    exam_task_number: ExamTaskNumber
    condition: str
    answer: str
    difficult: DifficultEnum


@dataclass(frozen=True, slots=True)
class CreateTaskResponse:
    id: UUID
    exam: ExamEnum
    subject: SubjectEnum
    exam_task_number: ExamTaskNumber
    condition: str
    answer: str
    difficult: DifficultEnum
    find_code: str
    task_sound_link: str | None
    task_file_link: str | None
    task_photo_link: str | None
    answer_video_link: str | None
    created_at: datetime


class CreateTaskInteractor:
    def __init__(
        self,
        task_data_gateway: TaskDataGateway,
        committer: Committer,
        task_service: TaskService,
    ):
        self._task_data_gateway = task_data_gateway
        self._committer = committer
        self._task_service = task_service

    async def __call__(self, request_data: CreateTaskRequest) -> CreateTaskResponse:
        logger.info("Create task: started. Condition: %s", request_data.condition)
        exam: ExamEnum = ExamEnum(request_data.exam)
        subject: SubjectEnum = SubjectEnum(request_data.subject)
        exam_task_number: ExamTaskNumber = ExamTaskNumber(request_data.exam_task_number)
        condition: Condition = Condition(request_data.condition)
        answer: StrAnswer = StrAnswer(request_data.answer)
        difficult: DifficultEnum = DifficultEnum(request_data.difficult)
        created_at: datetime | None = None
        task_sound_link: TaskSoundLink | None = None
        task_file_link: TaskFileLink | None = None
        task_photo_link: TaskPhotoLink | None = None
        answer_video_link: AnswerVideoLink | None = None
        task: Task = await self._task_service.create_task(
            exam=exam,
            subject=subject,
            exam_task_number=exam_task_number,
            condition=condition,
            answer=answer,
            difficult=difficult,
            created_at=created_at,
            task_sound_link=task_sound_link,
            task_file_link=task_file_link,
            task_photo_link=task_photo_link,
            answer_video_link=answer_video_link,
        )

        await self._task_data_gateway.add(task)

        await self._committer.commit()

        logger.info("Create task: finished. Condition: %s", task.condition)
        return CreateTaskResponse(
            id=task.id,
            exam=task.exam,
            subject=task.subject,
            exam_task_number=task.exam_task_number,
            condition=task.condition,
            answer=task.answer,
            difficult=task.difficult,
            find_code=task.find_code,
            task_sound_link=task.task_sound_link,
            task_file_link=task.task_file_link,
            task_photo_link=task.task_photo_link,
            answer_video_link=task.answer_video_link,
            created_at=task.created_at,
        )
