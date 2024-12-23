from abc import abstractmethod
from typing import Protocol


class Committer(Protocol):
    @abstractmethod
    def commit(self) -> None: ...
