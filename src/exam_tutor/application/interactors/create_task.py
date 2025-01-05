import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from uuid import UUID

from exam_tutor.application.enums import FileType
from exam_tutor.application.errors import NotCreated, ValidationError
from exam_tutor.application.interfaces.committer import Committer
from exam_tutor.application.interfaces.file_manager import FileManager
from exam_tutor.application.interfaces.task_data_gateway import TaskDataGateway
from exam_tutor.application.validators.check_mime_type import (
    check_answer_video_mime_type,
    check_task_file_mime_type,
    check_task_photo_mime_type,
    check_task_sound_mime_type,
)
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
from exam_tutor.domain.interfaces.generation_task_answer_video_link import (
    GenerationAnswerVideoLink,
)
from exam_tutor.domain.interfaces.generation_task_file_link import (
    GenerationTaskFileLink,
)
from exam_tutor.domain.interfaces.generation_task_photo_link import (
    GenerationTaskPhotoLink,
)
from exam_tutor.domain.interfaces.generation_task_sound_link import (
    GenerationTaskSoundLink,
)
from exam_tutor.domain.services.task import TaskService

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class CreateTaskRequest:
    exam: str
    subject: str
    exam_task_number: int
    condition: str
    answer: str
    difficult: str


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
    task_sound_links: list[str] | None
    task_file_links: list[str] | None
    task_photo_links: list[str] | None
    answer_video_link: str | None
    created_at: datetime


class CreateTaskInteractor:
    def __init__(
        self,
        task_data_gateway: TaskDataGateway,
        committer: Committer,
        task_service: TaskService,
        file_manager: FileManager,
        generation_task_sound_link: GenerationTaskSoundLink,
        generation_task_file_link: GenerationTaskFileLink,
        generation_task_photo_link: GenerationTaskPhotoLink,
        generation_answer_video_link: GenerationAnswerVideoLink,
    ):
        self._task_data_gateway = task_data_gateway
        self._committer = committer
        self._task_service = task_service
        self._file_manager = file_manager
        self._generation_task_sound_link = generation_task_sound_link
        self._generation_task_file_link = generation_task_file_link
        self._generation_task_photo_link = generation_task_photo_link
        self._generation_answer_video_link = generation_answer_video_link

    async def generate_link_and_save_sound_file(
        self, payload: bytes, content_type: str
    ) -> TaskSoundLink:
        logger.info("CHECK:: %s", content_type)
        if check_task_sound_mime_type(content_type=content_type):
            task_sound_link: TaskSoundLink = (
                await self._generation_task_sound_link.generate_task_sound_link()
            )
            sound_file_info = {
                "payload": payload,
                "content_type": content_type,
                "link": task_sound_link,
            }

            await self._file_manager.save_sound_file(file_info=sound_file_info)

            return task_sound_link
        else:
            raise ValidationError("Sound should be in [.wav, .mp3, .mpeg, .ogg]")

    async def generate_link_and_save_file_file(
        self, payload: bytes, content_type: str
    ) -> TaskFileLink:
        if check_task_file_mime_type(content_type=content_type):
            task_file_link = (
                await self._generation_task_file_link.generate_task_file_link()
            )

            file_file_info = {
                "payload": payload,
                "content_type": content_type,
                "link": task_file_link,
            }

            await self._file_manager.save_file_file(file_info=file_file_info)

            return task_file_link
        else:
            raise ValidationError(
                "File should be in [.txt, .docx, .doc, .pdf, .xlsx, .xlsm, .xls, .ods]"
            )

    async def generate_link_and_save_photo_file(
        self, payload: bytes, content_type: str
    ) -> TaskPhotoLink:
        if check_task_photo_mime_type(content_type=content_type):
            task_photo_link = (
                await self._generation_task_photo_link.generate_task_photo_link()
            )

            photo_file_info = {
                "payload": payload,
                "content_type": content_type,
                "link": task_photo_link,
            }

            await self._file_manager.save_photo_file(file_info=photo_file_info)

            return task_photo_link
        raise ValidationError("Photo should be in [.jpeg, .png, .jpg]")

    async def __call__(
        self,
        request_data: CreateTaskRequest,
        request_files: Dict[str, bytes | str | None],
    ) -> CreateTaskResponse:
        logger.info("Create task: started. Condition: %s", request_data.condition)
        try:
            exam: ExamEnum = ExamEnum(request_data.exam)
            subject: SubjectEnum = SubjectEnum(request_data.subject)
            exam_task_number: ExamTaskNumber = ExamTaskNumber(
                request_data.exam_task_number
            )
            condition: Condition = Condition(request_data.condition)
            answer: StrAnswer = StrAnswer(request_data.answer)
            difficult: DifficultEnum = DifficultEnum(request_data.difficult)
            created_at: datetime | None = None
            answer_video_link: AnswerVideoLink | None = None
            task_sound_file_links: list[TaskSoundLink] | None = None
            task_file_file_links: list[TaskFileLink] | None = None
            task_photo_file_links: list[TaskPhotoLink] | None = None

            if request_files[FileType.ANSWER_VIDEO] is not None:
                if check_answer_video_mime_type(
                    content_type=request_files[FileType.ANSWER_VIDEO].get(
                        "content_type"
                    )
                ):
                    answer_video_link: AnswerVideoLink = await (
                        self._generation_answer_video_link.generate_answer_video_link()
                    )
                    await self._file_manager.save_answer_video(
                        payload=request_files[FileType.ANSWER_VIDEO].get("payload"),
                        content_type=request_files[FileType.ANSWER_VIDEO].get(
                            "content_type"
                        ),
                        answer_video_link=answer_video_link,
                    )
                else:
                    raise ValidationError(
                        "Answer video should be in [.mp4, .webm, .avi, .mpeg, .egp, \
                         .3g2, .mov, .mkv, wmv, .flv, .ogv]"
                    )

            if request_files[FileType.SOUND] is not None:
                task_sound_file_links = list()
                for file in request_files[FileType.SOUND]:
                    task_sound_link = await self.generate_link_and_save_sound_file(
                        payload=file.get("payload"),
                        content_type=file.get("content_type"),
                    )

                    task_sound_file_links.append(task_sound_link)

            if request_files[FileType.FILE] is not None:
                task_file_file_links = list()
                for file in request_files[FileType.FILE]:
                    task_file_link = await self.generate_link_and_save_file_file(
                        payload=file.get("payload"),
                        content_type=file.get("content_type"),
                    )

                    task_file_file_links.append(task_file_link)

            if request_files[FileType.PHOTO] is not None:
                task_photo_file_links = list()
                for file in request_files[FileType.PHOTO]:
                    task_photo_link = await self.generate_link_and_save_photo_file(
                        payload=file.get("payload"),
                        content_type=file.get("content_type"),
                    )

                    task_photo_file_links.append(task_photo_link)

            task: Task = await self._task_service.create_task(
                exam=exam,
                subject=subject,
                exam_task_number=exam_task_number,
                condition=condition,
                answer=answer,
                difficult=difficult,
                created_at=created_at,
                task_sound_links=task_sound_file_links,
                task_file_links=task_file_file_links,
                task_photo_links=task_photo_file_links,
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
                task_sound_links=task.task_sound_links,
                task_file_links=task.task_file_links,
                task_photo_links=task.task_photo_links,
                answer_video_link=task.answer_video_link,
                created_at=task.created_at,
            )
        except Exception as error:
            logger.exception("Create task: raised %s", error)
            raise NotCreated(f"Not created. {error}") from None
