from injector import Module, provider, singleton, inject
from sqlalchemy.orm import sessionmaker

from pdv.config.default import Config
from pdv.config.dependencies import DBEngine, Session
from sqlalchemy import create_engine

from pdv.domain.establishment_service_interface import EstablishmentServiceInterface
from pdv.repository.establishment_repository import EstablishmentServiceRepository
from pdv.domain.transaction_service_interface import TransactionServiceInterface
from pdv.repository.transaction_repository import TransactionServiceRepository


class DbModule(Module):
    def configure(self, binder):
        binder.bind(EstablishmentServiceInterface, to=EstablishmentServiceRepository, scope=singleton)
        binder.bind(TransactionServiceInterface, to=TransactionServiceRepository, scope=singleton)

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
