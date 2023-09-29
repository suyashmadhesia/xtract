from enum import Enum
import os
from pathlib import Path
import yaml

from .postgres import Postgresql
from .mongo import MongoDB
from .abstract import DB


class Env(Enum):
    dev = 0
    staging = 1
    prod = 2


class DBConnection:

    pg_db = {}
    mongo_db = {}

    _instance = None

    def __new__(cls) -> 'DBConnection':
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.env = os.environ('XTRACT_ENV')
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
            for key, value in values.items():
                postgresql.__setattr__(key, value)
            self.pg_db[postgresql.name] = postgresql

    def _load_mongo_config(self, data: dict):
        if data is None:
            return
        for key, values in data.items():
            mongodb = MongoDB()
            mongodb.name = key
            for key, value in values.items():
                mongodb.__setattr__(key, value)
            self.mongo_db[mongodb.name] = mongodb

    def load_db_credentials(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        config_folder = os.path.join(BASE_DIR, 'db/config')
        config: dict
        if self.env == Env.staging.name:
            config = self._load_config_file(
                f'{config_folder}/staging-config.yml')
        elif self.env == Env.prod.name:
            config = self._load_config_file(f'{config_folder}/prod-config.yml')
        else:
            config = self._load_config_file(f'{config_folder}/dev-config.yml')
        self._load_postgres_config(config.get(DB.postgresql.value, None))
        self._load_mongo_config(config.get(DB.mongodb.value, None))
