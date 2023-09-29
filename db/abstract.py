from abc import ABC, abstractmethod


class DB(ABC):

    @abstractmethod
    def connect(self, config: dict) -> None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...
