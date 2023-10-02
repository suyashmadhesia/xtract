from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

from db.db_connection import DBConnection
from db.abstract import DB
from logger import info_logger, error_logger


Base = declarative_base()


class XMLFormatter(Base):
    __tablename__ = 'xml_formatter'

    id = Column(String(50), primary_key=True)


class HTMLFormatter(Base):
    __tablename__ = 'html_formatter'

    id = Column(String(50), primary_key=True)


class SourceDataStore(Base):
    __tablename__ = 'source_data_store'

    id = Column(String(50), primary_key=True)


class SQLModel:

    @staticmethod
    def migrate():
        try:
            info_logger.info(f'Trying creating table schema for {DBConnection.postgres[DB.raven.value].name} postgresql')
            Base.metadata.create_all(DBConnection.postgres[DB.raven.value].connection)
            info_logger.info(f'Successfully created table schema')
        except Exception as e:
            error_logger.error(f'Falied to creat table schema {DBConnection.postgres[DB.raven.value].name} {e}')
