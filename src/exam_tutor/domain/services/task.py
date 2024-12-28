from datetime import datetime

from exam_tutor.application.interfaces.generation_task_find_code import (
    GenerationTaskFindCode,
)
from exam_tutor.application.interfaces.generation_task_id import GenerationTaskId
from exam_tutor.domain.entities.task import (
    AnswerVideoLink,
    Condition,
    FindCode,
    StrAnswer,
    Task,
    TaskFileLink,
    TaskId,
    TaskPhotoLink,
    TaskSoundLink,
)
from exam_tutor.domain.enums import DifficultEnum, ExamEnum, ExamTaskNumber, SubjectEnum


class TaskService:
    def __init__(
        self,
        generation_task_id: GenerationTaskId,
        generation_find_code: GenerationTaskFindCode,
    ):
        self._generation_task_id = generation_task_id
        self._generation_find_code = generation_find_code

    async def create_task(
        self,
        exam: ExamEnum,
        subject: SubjectEnum,
        exam_task_number: ExamTaskNumber,
        condition: Condition,
        answer: StrAnswer,
        difficult: DifficultEnum,
        created_at: datetime | None,
        task_sound_link: TaskSoundLink | None,
        task_file_link: TaskFileLink | None,
        task_photo_link: TaskPhotoLink | None,
        answer_video_link: AnswerVideoLink | None,
    ):
        task_id: TaskId = await self._generation_task_id.generate_task_id()
        find_code: FindCode = await self._generation_find_code.generate_task_find_code()

        return Task(
            id=task_id,
            exam=exam,
            subject=subject,
            exam_task_number=exam_task_number,
            condition=condition,
            answer=answer,
            difficult=difficult,
            created_at=created_at,
            find_code=find_code,
            task_sound_link=task_sound_link,
            task_file_link=task_file_link,
            task_photo_link=task_photo_link,
            answer_video_link=answer_video_link,
        )
