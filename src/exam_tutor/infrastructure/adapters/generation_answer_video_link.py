from random import choices
from string import ascii_letters, digits

from exam_tutor.application.constants import TASK_ANSWER_VIDEO_LINK_LENGTH
from exam_tutor.domain.entities.task import AnswerVideoLink
from exam_tutor.domain.interfaces.generation_task_answer_video_link import (
    GenerationAnswerVideoLink,
)


class GenerationAnswerVideoLinkImpl(GenerationAnswerVideoLink):
    async def generate_answer_video_link(self) -> AnswerVideoLink:
        characters = ascii_letters + digits
        answer_video_link: AnswerVideoLink = AnswerVideoLink(
            "".join(choices(characters, k=TASK_ANSWER_VIDEO_LINK_LENGTH))
        )
        return answer_video_link
