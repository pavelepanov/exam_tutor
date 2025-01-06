from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class PostgresConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "PostgresConfig":
        uri = getenv("POSTGRES_URI")

        return PostgresConfig(str(uri))


@dataclass(frozen=True)
class MinIOConfig:
    uri: str
    access_key: str
    secret_key: str
    secure: bool
    minio_server: str

    @staticmethod
    def from_env() -> "MinIOConfig":
        uri = getenv("MINIO_URI")
        access_key = getenv("MINIO_ACCESS_KEY")
        secret_key = getenv("MINIO_SECRET_KEY")
        minio_server = getenv("MINIO_SERVER")
        if getenv("MINIO_SECURE") == "false":
            secure = False
        if getenv("MINIO_SECURE") == "true":
            secure = True

        return MinIOConfig(
            uri=uri,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
            minio_server=minio_server,
        )


@dataclass(frozen=True)
class S3Buckets:
    answer_video_bucket: str
    task_sound_bucket: str
    task_file_bucket: str
    task_photo_bucket: str

    @staticmethod
    def from_env() -> "S3Buckets":
        answer_video_bucket = getenv("ANSWER_VIDEO_BUCKET")
        task_sound_bucket = getenv("TASK_SOUND_BUCKET")
        task_file_bucket = getenv("TASK_FILE_BUCKET")
        task_photo_bucket = getenv("TASK_PHOTO_BUCKET")

        return S3Buckets(
            answer_video_bucket=answer_video_bucket,
            task_sound_bucket=task_sound_bucket,
            task_file_bucket=task_file_bucket,
            task_photo_bucket=task_photo_bucket,
        )


@dataclass(frozen=True)
class Config:
    minio_config: MinIOConfig
    postgres_config: PostgresConfig
    s3_buckets: S3Buckets


def create_config() -> Config:
    return Config(
        minio_config=MinIOConfig.from_env(),
        postgres_config=PostgresConfig.from_env(),
        s3_buckets=S3Buckets.from_env(),
    )
