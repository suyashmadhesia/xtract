import os
from pathlib import Path
import yaml
from typing import Dict

from .postgres import Postgresql
from .mongo import MongoDB
from .abstract import DB


class DBConnection:

    postgres : Dict[str, Postgresql] = {}
    mongoDB : Dict[str, MongoDB] = {}

    _instance = None

    def __new__(cls) -> 'DBConnection':
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.env = os.environ.get('XTRACT_ENV') or 'dev'
            return cls._instance
        return cls._instance

    def _load_config_file(self, path):
        config_dict: dict
        with open(path, 'r') as config:
            config_dict = yaml.safe_load(config)
        return config_dict

    def _load_postgres_config(self, data: dict):
        if data is None:
            return
        for key, values in data.items():
            postgresql = Postgresql()
            postgresql.name = key
            for k, value in values.items():
                postgresql.__setattr__(k, value)
            self.postgres[postgresql.name] = postgresql

    def _load_mongo_config(self, data: dict):
        if data is None:
            return
        for key, values in data.items():
            mongodb = MongoDB()
            mongodb.name = key
            for k, value in values.items():
                mongodb.__setattr__(k, value)
            self.mongoDB[mongodb.name] = mongodb

    def load_db_credentials(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        config_folder = os.path.join(BASE_DIR, 'db/config')
        config: dict = self._load_config_file(
                f'{config_folder}/{self.env}-config.yml')
        self._load_postgres_config(config.get(DB.postgresql.value, None))
        self._load_mongo_config(config.get(DB.mongodb.value, None))
