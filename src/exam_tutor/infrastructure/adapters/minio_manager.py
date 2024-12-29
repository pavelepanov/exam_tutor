from io import BytesIO

from minio import Minio

from exam_tutor.application.interfaces.file_manager import FileManager
from exam_tutor.entrypoint.config import Config


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
            self._minio_config.s3_answer_video_bucket,
            answer_video_link,
            BytesIO(payload),
            length=-1,
            content_type=content_type,
            part_size=5 * 1024 * 1024,
        )
