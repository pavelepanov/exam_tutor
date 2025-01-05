from exam_tutor.application.constants import (
    ANSWER_VIDEO_MIME_TYPE,
    TASK_FILE_MIME_TYPE,
    TASK_PHOTO_MIME_TYPE,
    TASK_SOUND_MIME_TYPE,
)


def check_task_file_mime_type(content_type: str) -> bool:
    return content_type in TASK_FILE_MIME_TYPE


def check_task_photo_mime_type(content_type: str) -> bool:
    return content_type in TASK_PHOTO_MIME_TYPE


def check_task_sound_mime_type(content_type: str) -> bool:
    return content_type in TASK_SOUND_MIME_TYPE


def check_answer_video_mime_type(content_type: str) -> bool:
    return content_type in ANSWER_VIDEO_MIME_TYPE
