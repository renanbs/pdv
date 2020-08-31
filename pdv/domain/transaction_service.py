from injector import inject

from pdv.repository.transaction_repository import TransactionRepository


class TransactionService:
    @inject
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(self, name: str):
        self.repository.save(name)
