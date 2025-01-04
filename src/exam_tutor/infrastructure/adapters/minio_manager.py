import logging
from io import BytesIO

from minio import Minio

from exam_tutor.application.interfaces.file_manager import FileManager
from exam_tutor.domain.entities.task import (
    AnswerVideoLink,
    TaskFileLink,
    TaskPhotoLink,
    TaskSoundLink,
)
from exam_tutor.entrypoint.config import Config

logger = logging.getLogger(__name__)


PART_SIZE = 5 * 1024 * 1024


async def create_public_url(minio_server: str, bucket_name: str, link: str) -> str:
    return f"http://{minio_server}/{bucket_name}/{link}"


class MinIOManager(FileManager):
    def __init__(
        self,
        minio_client: Minio,
        minio_config: Config,
    ):
        self._minio_client = minio_client
        self._minio_config = minio_config

    async def save_answer_video(
        self, payload: bytes, answer_video_link: str, content_type: str
    ) -> None:
        self._minio_client.put_object(
            self._minio_config.s3_buckets.answer_video_bucket,
            answer_video_link,
            BytesIO(payload),
            length=-1,
            content_type=content_type,
            part_size=PART_SIZE,
        )

    async def save_sound_file(
        self, file_info: dict[str, bytes | str | TaskSoundLink]
    ) -> None:
        self._minio_client.put_object(
            self._minio_config.s3_buckets.task_sound_bucket,
            file_info.get("link"),
            BytesIO(file_info.get("payload")),
            length=-1,
            content_type=file_info.get("content_type"),
            part_size=PART_SIZE,
        )

    async def save_file_file(
        self, file_info: dict[str, bytes | str | TaskFileLink]
    ) -> None:
        self._minio_client.put_object(
            self._minio_config.s3_buckets.task_file_bucket,
            file_info.get("link"),
            BytesIO(file_info.get("payload")),
            length=-1,
            content_type=file_info.get("content_type"),
            part_size=PART_SIZE,
        )

    async def save_photo_file(
        self, file_info: dict[str, bytes | str | TaskPhotoLink]
    ) -> None:
        self._minio_client.put_object(
            self._minio_config.s3_buckets.task_photo_bucket,
            file_info.get("link"),
            BytesIO(file_info.get("payload")),
            length=-1,
            content_type=file_info.get("content_type"),
            part_size=PART_SIZE,
        )

    async def get_answer_video_public_url(
        self, answer_video_link: AnswerVideoLink
    ) -> str:
        answer_video_public_url = await create_public_url(
            minio_server=self._minio_config.minio_config.minio_server,
            bucket_name=self._minio_config.s3_buckets.answer_video_bucket,
            link=answer_video_link,
        )

        return answer_video_public_url
