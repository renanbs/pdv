from abc import ABC, abstractmethod

from pdv.repository.establishment_model import Establishment


class EstablishmentServiceInterface(ABC):
    @abstractmethod
    def save(self, establishment: Establishment) -> None:
        pass

    @abstractmethod
    def list(self) -> list:
        pass

    @abstractmethod
    def find_by_cnpj(self, cnpj: str) -> Establishment:
        pass
