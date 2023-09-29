from .abstract import AbstractDB


class Postgresql(AbstractDB):

    def __init__(self):
        self.user: str
        self.password: str
        self.host: str
        self.port: str
        self.name: str

    def connect(self, config: dict) -> None:
        return super().connect(config)

    def disconnect(self) -> None:
        return super().disconnect()
        