from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy import Connection
from sqlalchemy.engine import URL

from .abstract import AbstractDB


class Postgresql(AbstractDB):
    '''
    Postgresql class which holds credentials and manage connections to
    database with given name.

    ...

    Attributes:
    -----------
    user: `str`
        username for database instance.
    password: `str`
        password for datanbase instance.
    port: `str`
        port for database instance but used as `int`.
    host: `str`
        host (e.g. localhost) for database instance.
    name: `str`
        represents database name.
    connection: `Connection`
        save the current connection to database for further use.

    Methods:
    --------
    `connect()`:
        responsible for creating engine and connecting to database instance
        and return instance of `Connection` object. Call this method only once
        use connection attribute to access `Connection` object.
    `disconnect()`:
        close database connection
    '''

    _drive_name: str = 'postgresql'

    def __init__(self):
        self.user: str
        self.password: str
        self.host: str
        self.port: str
        self.name: str

    def _create_engine(self) -> Engine:
        url = URL.create(drivername=self._drive_name, username=self.user,
                         password=self.password, host=self.host,
                         port=int(self.port), database=self.name)
        engine = create_engine(url)
        return engine

    def connect(self) -> Connection:
        engine = self._create_engine()
        self.connection = engine.connect()
        return self.connection

    def disconnect(self) -> None:
        self.connection.close()
