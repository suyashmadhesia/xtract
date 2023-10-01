from mongoengine import connect, disconnect

from .abstract import AbstractDB
from logger import info_logger, error_logger


class MongoDB(AbstractDB):

    '''
    MongoDB class which holds credentials and manage connections to
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

    def __init__(self):
        self.user: str
        self.password: str
        self.host: str
        self.port: str
        self.name: str
        self.connection = None

    def connect(self) -> None:
        try:
            info_logger.info(f'Connecting to database {self.name} Mongo.....')
            self.connection = connect(db=self.name, alias=self.name, username=self.user,
                                      password=self.password, host=self.host, port=self.port)
            info_logger.info(f'Connected successfully to database')
            return self.connection
        except Exception as e:
            error_logger.error(f'Unable to connect getting erorr {e}')

    def disconnect(self) -> None:
        try:
            info_logger.info(f'Closing connection from {self.name} Mongo....')
            disconnect(self.name)
            info_logger.info(
                f'Closed connection successfully from {self.name} Mongo')
        except Exception as e:
            error_logger.error(f'Unable to close connection {e}')
