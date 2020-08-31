from abc import ABC, abstractmethod

from pdv.repository.transaction_model import Transaction


class TransactionServiceInterface(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        pass
