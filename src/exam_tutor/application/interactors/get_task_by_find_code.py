import logging
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from exam_tutor.application.errors import DoesNotExistError
from exam_tutor.application.interfaces.file_manager import FileManager
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
    task_sound_urls: list[str] | None
    task_file_urls: list[str] | None
    task_photo_urls: list[str] | None
    answer_video_public_url: str | None
    created_at: datetime


class GetTaskByFindCodeInteractor:
    def __init__(
        self,
        task_data_gateway: TaskDataGateway,
        file_manager: FileManager,
    ):
        self._task_data_gateway = task_data_gateway
        self._file_manager = file_manager

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
            answer_video_public_url: str | None = None
            task_sound_urls: list[str] | None = None
            task_files_urls: list[str] | None = None
            task_photo_urls: list[str] | None = None

            if task.answer_video_link is not None:
                answer_video_public_url = (
                    await self._file_manager.get_answer_video_public_url(
                        answer_video_link=task.answer_video_link
                    )
                )

            if task.task_sound_links is not None:
                task_sound_urls = list()
                for task_sound_link in task.task_sound_links:
                    task_sound_file_url = (
                        await self._file_manager.get_task_sound_file_public_url(
                            task_sound_file_link=task_sound_link
                        )
                    )
                    task_sound_urls.append(task_sound_file_url)

            if task.task_file_links is not None:
                task_files_urls = list()
                for task_file_link in task.task_file_links:
                    task_file_url = (
                        await self._file_manager.get_task_file_file_public_url(
                            task_file_file_link=task_file_link
                        )
                    )
                    task_files_urls.append(task_file_url)

            if task.task_photo_links is not None:
                task_photo_urls = list()
                for task_photo_link in task.task_photo_links:
                    task_photo_url = (
                        await self._file_manager.get_task_photo_file_public_url(
                            task_photo_file_link=task_photo_link
                        )
                    )
                    task_photo_urls.append(task_photo_url)

            logger.info("Get task by find code: finished. Find code: %s", find_code)
            return GetTaskByFindCodeResponse(
                id=task.id,
                exam=task.exam,
                subject=task.subject,
                exam_task_number=task.exam_task_number,
                condition=task.condition,
                answer=task.answer,
                difficult=task.difficult,
                task_sound_urls=task_sound_urls,
                task_file_urls=task_files_urls,
                task_photo_urls=task_photo_urls,
                answer_video_public_url=answer_video_public_url,
                created_at=task.created_at,
                find_code=task.find_code,
            )
        else:
            logger.info(
                "Get task by find code: raised does not exist. Find code: %s", find_code
            )
            raise DoesNotExistError("Does not exist.")
