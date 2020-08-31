from abc import ABC, abstractmethod


class EstablishmentInterface(ABC):
    @abstractmethod
    def create_establishment(self, name: str) -> None:
        pass
