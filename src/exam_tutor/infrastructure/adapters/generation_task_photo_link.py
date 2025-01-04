from random import choices
from string import ascii_letters, digits

from exam_tutor.application.constants import TASK_PHOTO_LINK_WITHOUT_PREFIX_LENGTH
from exam_tutor.domain.entities.task import TaskPhotoLink
from exam_tutor.domain.interfaces.generation_task_photo_link import (
    GenerationTaskPhotoLink,
)


class GenerationTaskPhotoLinkImpl(GenerationTaskPhotoLink):
    async def generate_task_photo_link(self) -> TaskPhotoLink:
        characters = ascii_letters + digits
        task_photo_link: TaskPhotoLink = TaskPhotoLink(
            "task_photo_link"
            + "".join(choices(characters, k=TASK_PHOTO_LINK_WITHOUT_PREFIX_LENGTH))
        )
        return task_photo_link
