import os
import yaml

from unittest import TestCase
from unittest.mock import Mock
from pathlib import Path

from db.db_connection import DBConnection
from db.abstract import *
from db.postgres import Postgresql
from db.mongo import MongoDB

env = os.environ.get('XTRACT_ENV', 'dev')


def load_config_file():
    BASE_DIR = Path(__file__).resolve().parent.parent
    config_folder = os.path.join(BASE_DIR, 'db/config')
    config_dict: dict
    path = f'{config_folder}/{env}-config.yml'
    with open(path, 'r') as config:
        config_dict = yaml.safe_load(config)
    return config_dict


class TestDBConnectionPostgresConfig(TestCase):

    def setUp(self) -> None:
        self.db_connection = DBConnection()
        self.db_connection.load_db_credentials()
        self.config_dict = load_config_file()
        return super().setUp()

    def test_load_postgres_config(self):
        with self.assertRaises(ValueError):
            self.db_connection._load_postgres_config({})


    def test_db_config(self):
        self.assertEqual(type(self.config_dict), dict)
        self.assertIn('postgresql', self.config_dict)
        

    def test_postgresql_raven_config(self):
        postgres_config = self.config_dict['postgresql']
        self.assertEqual(
            type(self.db_connection.postgres['raven']), Postgresql)
        self.assertIn('raven', postgres_config)
        self.assertEqual(type(postgres_config['raven']), dict)
        self.assertEqual(
            postgres_config['raven']['user'], self.db_connection.postgres['raven'].user)
        self.assertEqual(
            postgres_config['raven']['password'], self.db_connection.postgres['raven'].password)
        self.assertEqual(
            postgres_config['raven']['host'], self.db_connection.postgres['raven'].host)
        self.assertEqual(
            postgres_config['raven']['port'], self.db_connection.postgres['raven'].port)
        self.assertEqual('raven', self.db_connection.postgres['raven'].name)


class TestConnectionMongoConfig(TestCase):

    def setUp(self) -> None:
        self.db_connection = DBConnection()
        self.db_connection.load_db_credentials()
        self.config_dict = load_config_file()
        return super().setUp()

    def test_load_mongo_config(self):
        with self.assertRaises(ValueError):
            self.db_connection._load_mongo_config({})

    def test_db_config(self):
        self.assertEqual(type(self.config_dict), dict)
        self.assertIn('mongodb', self.config_dict)

    def test_mongo_raven_config(self):
        mongo_config = self.config_dict['mongodb']
        self.assertEqual(
            type(self.db_connection.mongoDB['raven']), MongoDB)
        self.assertIn('raven', mongo_config)
        self.assertEqual(type(mongo_config['raven']), dict)
        self.assertEqual(
            mongo_config['raven']['user'], self.db_connection.mongoDB['raven'].user)
        self.assertEqual(
            mongo_config['raven']['password'], self.db_connection.mongoDB['raven'].password)
        self.assertEqual(
            mongo_config['raven']['host'], self.db_connection.mongoDB['raven'].host)
        self.assertEqual(
            mongo_config['raven']['port'], self.db_connection.mongoDB['raven'].port)
        self.assertEqual('raven', self.db_connection.mongoDB['raven'].name)

    def test_mongo_xtract_config(self):
        mongo_config = self.config_dict['mongodb']
        self.assertEqual(
            type(self.db_connection.mongoDB['xtract']), MongoDB)
        self.assertIn('xtract', mongo_config)
        self.assertEqual(type(mongo_config['xtract']), dict)
        self.assertEqual(
            mongo_config['xtract']['user'], self.db_connection.mongoDB['xtract'].user)
        self.assertEqual(
            mongo_config['xtract']['password'], self.db_connection.mongoDB['xtract'].password)
        self.assertEqual(
            mongo_config['xtract']['host'], self.db_connection.mongoDB['xtract'].host)
        self.assertEqual(
            mongo_config['xtract']['port'], self.db_connection.mongoDB['xtract'].port)
        self.assertEqual('xtract', self.db_connection.mongoDB['xtract'].name)


class TestRavenConnection(TestCase):

    def setUp(self) -> None:
        self.db_connection = DBConnection()
        self.db_connection.load_db_credentials()
        self.raven_postgres = DBConnection.postgres[DB.raven.value]
        self.mock_engine = Mock()
        self.mock_connection = Mock()
        self.raven_postgres._create_engine = Mock(
            return_value=self.mock_engine)
        return super().setUp()

    def test_postgres_connection(self):
        connection = self.raven_postgres.connect()
        self.raven_postgres._create_engine.assert_called_once_with()
        self.mock_engine.connect.assert_called_once_with()
        self.assertIs(connection, self.mock_engine.connect.return_value)


    def test_postgres_disconnect(self):
        self.raven_postgres.connect()
        self.raven_postgres.disconnect()
        self.mock_engine.connect.return_value.close.assert_called_once_with()

class TestXtractConnection(TestCase):
    ...
