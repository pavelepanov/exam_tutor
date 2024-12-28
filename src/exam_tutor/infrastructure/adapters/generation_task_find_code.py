from random import choices
from string import ascii_letters, digits

from exam_tutor.application.constants import TASK_FIND_CODE_LENGTH
from exam_tutor.domain.entities.task import FindCode
from exam_tutor.domain.interfaces.generation_task_find_code import (
    GenerationTaskFindCode,
)


class GenerationTaskFindCodeImpl(GenerationTaskFindCode):
    async def generate_task_find_code(self) -> FindCode:
        characters = ascii_letters + digits
        find_code: FindCode = FindCode(
            "".join(choices(characters, k=TASK_FIND_CODE_LENGTH))
        )
        return find_code
