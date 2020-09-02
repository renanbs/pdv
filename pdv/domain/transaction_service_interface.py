from abc import ABC, abstractmethod
from decimal import Decimal

from pdv.repository.transaction_model import Transaction


class TransactionServiceInterface(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_transactions_from_establishment_with_sum(self, cnpj: str) -> (list, Decimal):
        pass

    @abstractmethod
    def get_transactions(self, cnpj: str) -> list:
        pass
