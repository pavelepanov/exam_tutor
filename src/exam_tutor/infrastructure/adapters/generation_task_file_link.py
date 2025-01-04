from random import choices
from string import ascii_letters, digits

from exam_tutor.application.constants import TASK_FILE_LINK_WITHOUT_PREFIX_LENGTH
from exam_tutor.domain.entities.task import TaskFileLink
from exam_tutor.domain.interfaces.generation_task_file_link import (
    GenerationTaskFileLink,
)


class GenerationTaskFileLinkImpl(GenerationTaskFileLink):
    async def generate_task_file_link(self) -> TaskFileLink:
        characters = ascii_letters + digits
        task_file_link: TaskFileLink = TaskFileLink(
            "task_file_link"
            + "".join(choices(characters, k=TASK_FILE_LINK_WITHOUT_PREFIX_LENGTH))
        )
        return task_file_link
