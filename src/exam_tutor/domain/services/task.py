from datetime import datetime

from exam_tutor.domain.entities.task import (
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
from exam_tutor.domain.interfaces.generation_task_answer_video_link import (
    GenerationAnswerVideoLink,
)
from exam_tutor.domain.interfaces.generation_task_find_code import (
    GenerationTaskFindCode,
)
from exam_tutor.domain.interfaces.generation_task_id import GenerationTaskId


class TaskService:
    def __init__(
        self,
        generation_task_id: GenerationTaskId,
        generation_find_code: GenerationTaskFindCode,
        generation_task_answer_video_link: GenerationAnswerVideoLink,
    ):
        self._generation_task_id = generation_task_id
        self._generation_find_code = generation_find_code
        self._generation_task_answer_video_link = generation_task_answer_video_link

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
    ):
        task_id: TaskId = await self._generation_task_id.generate_task_id()
        find_code: FindCode = await self._generation_find_code.generate_task_find_code()
        answer_video_link = (
            await self._generation_task_answer_video_link.generate_answer_video_link()
        )

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
