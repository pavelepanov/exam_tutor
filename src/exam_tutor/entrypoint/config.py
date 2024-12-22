from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class PostgresConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "PostgresConfig":
        uri = getenv("POSTGRES_URI")

        return PostgresConfig(uri)