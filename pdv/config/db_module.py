from injector import Module, provider, singleton, inject
from sqlalchemy.orm import sessionmaker

from pdv.config.default import Config
from pdv.config.dependencies import DBEngine, Session
from sqlalchemy import create_engine

from pdv.domain.establishment_interface import EstablishmentInterface
from pdv.domain.transaction_interface import TransactionInterface
from pdv.repository.establishment_repository import EstablishmentRepository
from pdv.repository.transaction_repository import TransactionRepository


class DbModule(Module):
    def configure(self, binder):
        binder.bind(EstablishmentInterface, to=EstablishmentRepository, scope=singleton)
        binder.bind(TransactionInterface, to=TransactionRepository, scope=singleton)

    @provider
    @singleton
    def engine(self) -> DBEngine:
        engine = create_engine(Config.DB_URL, echo=True)
        engine.connect()
        return engine

    @provider
    @singleton
    @inject
    def session(self, engine: DBEngine) -> Session:
        session = sessionmaker(bind=engine)
        return session()
