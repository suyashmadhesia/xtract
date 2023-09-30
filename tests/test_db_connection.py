import os
import yaml

from unittest import TestCase
from pathlib import Path

from db.db_connection import DBConnection
from db.abstract import *
from db.postgres import Postgresql
from db.mongo import MongoDB


def load_config_file(env):
    BASE_DIR = Path(__file__).resolve().parent.parent
    config_folder = os.path.join(BASE_DIR, 'db/config')
    config_dict: dict
    path = f'{config_folder}/{env}-config.yml'
    with open(path, 'r') as config:
        config_dict = yaml.safe_load(config)
    return config_dict


class TestDBConnectionPostgres(TestCase):

    def setUp(self) -> None:
        self.db_connection = DBConnection()
        self.db_connection.load_db_credentials()
        self.env = 'dev'  # TODO  check using environment variable
        return super().setUp()

    def test_db_config(self):
        self.config_dict = load_config_file(self.env)
        self.assertEqual(type(self.config_dict), dict)
        self.assertIn('postgresql', self.config_dict)

    def test_postgresql_raven_config(self):
        self.config_dict = load_config_file(self.env)
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

    def test_postgresql_xtract_config(self):
        self.config_dict = load_config_file(self.env)
        postgres_config = self.config_dict['postgresql']
        self.assertEqual(
            type(self.db_connection.postgres['xtract']), Postgresql)
        self.assertIn('xtract', postgres_config)
        self.assertEqual(type(postgres_config['xtract']), dict)
        self.assertEqual(
            postgres_config['xtract']['user'], self.db_connection.postgres['xtract'].user)
        self.assertEqual(
            postgres_config['xtract']['password'], self.db_connection.postgres['xtract'].password)
        self.assertEqual(
            postgres_config['xtract']['host'], self.db_connection.postgres['xtract'].host)
        self.assertEqual(
            postgres_config['xtract']['port'], self.db_connection.postgres['xtract'].port)
        self.assertEqual('xtract', self.db_connection.postgres['xtract'].name)


class TestConnectionMongo(TestCase):

    def setUp(self) -> None:
        self.db_connection = DBConnection()
        self.db_connection.load_db_credentials()
        self.env = 'dev'  # TODO  check using environment variable
        return super().setUp()

    def test_db_config(self):
        self.config_dict = load_config_file(self.env)
        self.assertEqual(type(self.config_dict), dict)
        self.assertIn('mongodb', self.config_dict)

    def test_mongo_raven_config(self):
        self.config_dict = load_config_file(self.env)
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
        self.config_dict = load_config_file(self.env)
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
