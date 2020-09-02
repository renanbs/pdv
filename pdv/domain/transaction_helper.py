from injector import inject

from pdv.domain.establishment_schema import EstablishmentSchema
from pdv.domain.establishment_service import EstablishmentService
from pdv.domain.transaction_schema import TransactionSchema
from pdv.domain.transaction_service import TransactionService
from pdv.repository.transaction_model import Transaction


class TransactionHelper:
    @inject
    def __init__(self, transaction_service: TransactionService, ec_service: EstablishmentService):
        self.transaction_service = transaction_service
        self.ec_service = ec_service

    def create_transaction(self, transaction: Transaction) -> None:
        self.transaction_service.create_transaction(transaction)

    def get_transactions_from_establishment(self, cnpj: str) -> dict:
        ec = self.ec_service.get_establishment(cnpj)
        transactions, _sum = self.transaction_service.get_transactions_from_establishment_with_sum(cnpj)
        return {
            'estabelecimento': EstablishmentSchema().dump(ec),
            'total_recebido': str(_sum),
            'recebimentos': TransactionSchema().dump(transactions, many=True)
        }
