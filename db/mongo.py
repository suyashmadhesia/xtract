from .abstract import DB


class MongoDB(DB):

    def connect(self, config: dict) -> None:
        return super().connect(config)

    def disconnect(self) -> None:
        return super().disconnect()
