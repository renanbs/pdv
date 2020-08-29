from injector import Module, singleton, provider

from pdv.api.app_establishments import EstablishmentsEndpoint
from pdv.api.app_transactions import TransactionsEndpoint
from pdv.default import Config
from pdv.dependencies import ApplicationRegister, ApplicationConfig


class AppModule(Module):
    @singleton
    @provider
    def register(self) -> ApplicationRegister:
        return [TransactionsEndpoint, EstablishmentsEndpoint]

    @provider
    def configuration(self) -> ApplicationConfig:
        return Config
