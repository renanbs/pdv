from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# from pdv.config.db_module import Base

Base = declarative_base()


class Establishment(Base):
    __tablename__ = 'establishment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
