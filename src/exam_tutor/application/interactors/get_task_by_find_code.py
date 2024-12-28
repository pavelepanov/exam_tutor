import logging
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from exam_tutor.application.errors import DoesNotExistError
from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.domain.entities.task import FindCode, Task
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class GetTaskByFindCodeRequest:
    find_code: str


@dataclass(frozen=True, slots=True)
class GetTaskByFindCodeResponse:
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


class GetTaskByFindCodeInteractor:
    def __init__(
        self,
        task_data_gateway: TaskDataGateway,
    ):
        self._task_data_gateway = task_data_gateway

    async def __call__(
        self, request_data: GetTaskByFindCodeRequest
    ) -> GetTaskByFindCodeResponse:
        logger.info(
            "Get task by find code: started. Find code: %s", request_data.find_code
        )
        find_code: FindCode = FindCode(request_data.find_code)

        task: Task = await self._task_data_gateway.read_by_find_code(
            find_code=find_code
        )

        if task is not None:
            logger.info("Get task by find code: finished. Find code: %s", find_code)
            return GetTaskByFindCodeResponse(
                id=task.id,
                exam=task.exam,
                subject=task.subject,
                exam_task_number=task.exam_task_number,
                condition=task.condition,
                answer=task.answer,
                difficult=task.difficult,
                task_sound_link=task.task_sound_link,
                task_file_link=task.task_file_link,
                task_photo_link=task.task_photo_link,
                answer_video_link=task.answer_video_link,
                created_at=task.created_at,
                find_code=task.find_code,
            )
        else:
            logger.info(
                "Get task by find code: raised does not exist. Find code: %s", find_code
            )
            raise DoesNotExistError("Does not exist.")
