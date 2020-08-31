from injector import inject

from pdv.repository.transaction_model import Transaction
from pdv.repository.transaction_repository import TransactionServiceRepository


class TransactionService:
    @inject
    def __init__(self, repository: TransactionServiceRepository):
        self.repository = repository

    def create_transaction(self, transaction: Transaction) -> None:
        self.repository.save(transaction)
