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
