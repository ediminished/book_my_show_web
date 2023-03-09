from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.orm import declarative_base
import sqlalchemy
from .db_engine import DBEngine

Base = declarative_base(cls=DeferredReflection)


class TestTable(Base):
    __tablename__ = "test_table"
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    age = sqlalchemy.Column("age", sqlalchemy.Integer)


def create_db_models():
    engine = DBEngine.get_db_engine()
    Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
    Base.prepare(engine)


create_db_models()
