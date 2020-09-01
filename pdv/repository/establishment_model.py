from pycpfcnpj import cpfcnpj
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import validates


Base = declarative_base()


class Establishment(Base):
    __tablename__ = 'establishment'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    cnpj = Column(String(14), nullable=False, unique=True)
    dono = Column(String(50), nullable=False)
    telefone = Column(String(11), nullable=False)

    @validates('cnpj')
    def validate_cnpj(self, key, cnpj) -> str:
        if not len(cnpj) == 14:
            raise ValueError('invalid cnpj')
        if not cpfcnpj.validate(cnpj):
            raise ValueError('invalid cnpj')
        return cnpj
