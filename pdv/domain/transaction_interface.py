from abc import ABC, abstractmethod


class TransactionInterface(ABC):
    @abstractmethod
    def create_transaction(self, name: str) -> None:
        pass
