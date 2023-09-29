from .postgres import Postgresql
from .mongo import MongoDB

class BDConnection:

    def __init__(self, config: dict) -> None:
        self.config = config
        self.postgresql = Postgresql()
        self.mongodb = MongoDB()
        
        
