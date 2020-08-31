from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from pdv.repository.establishment_model import Establishment

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    descricao = Column(String)
    valor = Column(Numeric)
    cliente = Column(String)
    estabelecimento = Column(String, ForeignKey(Establishment.cnpj), nullable=False)
