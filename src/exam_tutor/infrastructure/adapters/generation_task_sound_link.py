from random import choices
from string import ascii_letters, digits

from exam_tutor.application.constants import TASK_SOUND_LINK_WITHOUT_PREFIX_LENGTH
from exam_tutor.domain.entities.task import TaskSoundLink
from exam_tutor.domain.interfaces.generation_task_sound_link import (
    GenerationTaskSoundLink,
)


class GenerationTaskSoundLinkImpl(GenerationTaskSoundLink):
    async def generate_task_sound_link(self) -> TaskSoundLink:
        characters = ascii_letters + digits
        task_sound_link: TaskSoundLink = TaskSoundLink(
            "task_sound_link"
            + "".join(choices(characters, k=TASK_SOUND_LINK_WITHOUT_PREFIX_LENGTH))
        )
        return task_sound_link
