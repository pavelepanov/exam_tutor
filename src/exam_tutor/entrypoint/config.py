from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class PostgresDsn:
    db_uri: str

    @staticmethod
    def from_env() -> "PostgresDsn":
        uri = getenv("POSTGRES_URI")

        return PostgresDsn(str(uri))


@dataclass(frozen=True)
class MinIOConfig:
    uri: str
    access_key: str
    secret_key: str
    secure: bool

    @staticmethod
    def from_env() -> "MinIOConfig":
        uri = getenv("MINIO_URI")
        access_key = getenv("MINIO_ACCESS_KEY")
        secret_key = getenv("MINIO_SECRET_KEY")
        secure = getenv("MINIO_SECURE")

        return MinIOConfig(
            uri=uri, access_key=access_key, secret_key=secret_key, secure=secure
        )


@dataclass(frozen=True)
class Config:
    s3_answer_video_bucket: str
