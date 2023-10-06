from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from datetime import datetime

from .db_connection import DBConnection
from .abstract import DB
from logger import info_logger, error_logger
import utils


Base = declarative_base()


class XMLFormatter(Base):
    __tablename__ = 'xml_formatter'

    id = Column(String(36), primary_key=True, default=utils.generate_id)


class HTMLFormatter(Base):
    __tablename__ = 'html_formatter'

    id = Column(String(36), primary_key=True, default=utils.generate_id)


class SourceDataStore(Base):
    __tablename__ = 'source_data_store'

    id = Column(String(36), primary_key=True, default=utils.generate_id)
    name = Column(String(50), nullable=False, unique=True)
    scraped_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    url = Column(String(2000),  nullable=False, unique=True)
    is_rss = Column(Boolean(), default=False)
    xml_formattor = Column(String(36), ForeignKey(
        'xml_formatter.id'), nullable=True)
    html_formattor = Column(String(36), ForeignKey(
        'html_formatter.id'), nullable=True)


class SQLModel:

    @staticmethod
    def migrate():
        try:
            info_logger.info(
                f'Trying creating table schema for {DBConnection.postgres[DB.raven.value].name} postgresql')
            Base.metadata.create_all(
                DBConnection.postgres[DB.raven.value].connection.engine)
            info_logger.info(f'Successfully created table schema')
        except Exception as e:
            error_logger.error(
                f'Falied to creat table schema {DBConnection.postgres[DB.raven.value].name} {e}')
