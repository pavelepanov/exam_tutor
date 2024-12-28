from uuid import uuid4

from exam_tutor.domain.entities.task import TaskId
from exam_tutor.domain.interfaces.generation_task_id import GenerationTaskId


class GenerationTaskIdImpl(GenerationTaskId):
    async def generate_task_id(self) -> TaskId:
        task_id = TaskId(uuid4())
        return task_id
