from abc import ABC, abstractmethod


class EstablishmentInterface(ABC):
    @abstractmethod
    def save(self, name: str) -> None:
        pass
