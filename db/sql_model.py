from sqlalchemy.orm import DeclarativeBase

from db.db_connection import DBConnection
from db.abstract import DB


class Base(DeclarativeBase):
    pass


class XMLFormatter(DeclarativeBase):
    __tablename__ = 'xml_formatter'


class HTMLFormatter(DeclarativeBase):
    __tablename__ = 'html_formatter'


class SourceDataStore(DeclarativeBase):
    __tablename__ = 'source_data_store'


Base.metadata.create_all(DBConnection.postgres[DB.raven.value])