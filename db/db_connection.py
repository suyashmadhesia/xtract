import os
from pathlib import Path
import yaml
from typing import Dict

from .postgres import Postgresql
from .mongo import MongoDB
from .abstract import DB
from logger import error_logger, info_logger


# TODO: Documentation for this class is left.

class DBConnection:

    postgres: Dict[str, Postgresql] = {}
    mongoDB: Dict[str, MongoDB] = {}

    _instance = None

    def __new__(cls) -> 'DBConnection':
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.env = os.environ.get('XTRACT_ENV', 'dev')
            return cls._instance
        return cls._instance

    def _load_config_file(self, path):
        try:
            info_logger.info(f'Loading configuration from {path}')
            config_dict: dict
            with open(path, 'r') as config:
                config_dict = yaml.safe_load(config)
            return config_dict
        except Exception as e:
            error_logger.error(f'Getting error while loading file {path} {e}')
            raise e

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

    # TODO: Implement unittests for these two functions.

    @classmethod
    def connect_dbs(cls):
        for i in cls.postgres:
            cls.postgres[i].connect()
        for i in cls.mongoDB:
            cls.mongoDB[i].connect()

    @classmethod
    def disconnect_dbs(cls):
        for i in cls.postgres:
            cls.postgres[i].disconnect()
        for i in cls.mongoDB:
            cls.mongoDB[i].disconnect()
