from abc import ABC, abstractmethod


class TransactionInterface(ABC):
    @abstractmethod
    def save(self, name: str) -> None:
        pass
