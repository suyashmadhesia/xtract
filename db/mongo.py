from mongoengine import connect, disconnect

from .abstract import AbstractDB


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
        self.connection = connect(db=self.name, alias=self.name, username=self.user,
                                  password=self.password, host=self.host, port=self.port)
        return self.connection

    def disconnect(self) -> None:
        disconnect(self.name)
        return super().disconnect()
