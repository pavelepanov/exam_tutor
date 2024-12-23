from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from exam_tutor.application.interfaces.committer import Committer
from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.entities.task import Task, TaskId
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum


@dataclass(frozen=True, slots=True)
class GetTaskByUUIDRequest:
    id: int


@dataclass(frozen=True, slots=True)
class GetTaskByUUIDResponse:
    id: int
    exam: ExamEnum
    subject: SubjectEnum
    exam_task_number: ExamTaskNumber
    condition: str
    answer: float | str
    difficult: DifficultEnum
    task_sound_id: UUID | None
    task_file_id: UUID | None
    task_photo_id: UUID | None
    answer_video_id: UUID | None
    created_at: datetime


class GetTaskByUUIDInteractor:
    def __init__(
        self,
        task_data_gateway: TaskDataGateway,
        committer: Committer,
    ):
        self._task_data_gateway = task_data_gateway
        self._committer = committer

    async def __call__(
        self, request_data: GetTaskByUUIDRequest
    ) -> GetTaskByUUIDResponse:
        task_id: TaskId = TaskId(request_data.id)

        task: Task = await self._task_data_gateway.read_by_uuid(id=task_id)

        return GetTaskByUUIDResponse(
            id=task.id,
            exam=task.exam,
            subject=task.subject,
            exam_task_number=task.exam_task_number,
            condition=task.condition,
            answer=task.answer,
            difficult=task.difficult,
            task_sound_id=task.task_sound_id,
            task_file_id=task.task_file_id,
            task_photo_id=task.task_photo_id,
            answer_video_id=task.answer_video_id,
            created_at=task.created_at,
        )
