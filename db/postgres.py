from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy import Connection
from sqlalchemy.engine import URL
from dataclasses import dataclass

from .abstract import AbstractDB
from logger import info_logger, error_logger


@dataclass
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

    user: str
    password: str
    host: str
    port: str
    name: str
    connection: Connection = None
    _driver_name: str = 'postgresql'

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)

    def _create_engine(self) -> Engine:
        info_logger.info(
            f'Creating engine using {self._driver_name} driver for database {self.name}')
        url = URL.create(drivername=self._driver_name, username=self.user,
                         password=self.password, host=self.host,
                         port=int(self.port), database=self.name)
        engine = create_engine(url)
        return engine

    def connect(self) -> Connection:
        try:
            engine = self._create_engine()
            info_logger.info(
                f'Connecting to database {self.name} {self._driver_name}....')
            self.connection = engine.connect()
            info_logger.info(
                f'Connected succesfully to database {self.name} {self._driver_name}')
            return self.connection
        except Exception as e:
            info_logger.error(f'Enable to establised connection got error {e}')

    def disconnect(self) -> None:
        try:
            info_logger.info(
                f'Closing connection from {self.name} {self._driver_name}')
            self.connection.close()
            info_logger.info('Closed successfully')
        except Exception as e:
            error_logger.error(
                f'Unable to close connection {self._driver_name} {self.name} {e}')
