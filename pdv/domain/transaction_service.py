from injector import inject

from pdv.domain.transaction_service_interface import TransactionServiceInterface
from pdv.repository.transaction_model import Transaction


class TransactionService:
    @inject
    def __init__(self, repository: TransactionServiceInterface):
        self.repository = repository

    def create_transaction(self, transaction: Transaction) -> None:
        self.repository.save(transaction)

    def get_transactions_from_establishment_with_sum(self, cnpj: str) -> dict:
        return self.repository.get_transactions_from_establishment_with_sum(cnpj)
