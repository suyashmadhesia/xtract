from abc import ABC, abstractmethod
from enum import Enum
from sqlalchemy import Connection


class DB(Enum):
    '''
    DB enum holds all the information related to databases
    1. kind of database (e.g. SQL, Postgresql, etc.)
        a. postgresql
        b. mongodb
    2. database names:
        a. raven
        b. xtract
    '''

    postgresql = 'postgresql'
    mongodb = 'mongodb'
    raven = 'raven'
    xtract = 'xtract'


class AbstractDB(ABC):
    '''
    Abstract class for databases each database which is used in 
    this project implement this class and implement its methods

    ...

    Methods:
    --------
    `connect()`: `Connection | None`
        method to connect to database
    `disconnect()`: `None`
        method for disconnecting from database
    '''

    @abstractmethod
    def connect(self) -> Connection | None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...
