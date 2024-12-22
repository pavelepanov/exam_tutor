from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class PostgresDsn:
    db_uri: str

    @staticmethod
    def from_env() -> "PostgresDsn":
        uri = getenv("POSTGRES_URI")

        return PostgresDsn(uri)