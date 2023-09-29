from abc import ABC, abstractmethod
from enum import Enum

class DB(Enum):
    postgresql = 'postgresql'
    mongodb = 'mongodb'
    raven = 'raven'
    xtract = 'xtract'


class AbstractDB(ABC):

    @abstractmethod
    def connect(self, config: dict) -> None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...
