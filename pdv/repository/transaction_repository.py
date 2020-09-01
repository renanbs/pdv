from decimal import Decimal

from injector import inject
from sqlalchemy import func

from pdv.config.dependencies import Session
from pdv.domain.transaction_service_interface import TransactionServiceInterface
from pdv.repository.exceptions import RepositoryException

from pdv.repository.transaction_model import Transaction


class TransactionServiceRepository(TransactionServiceInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def save(self, transaction: Transaction) -> None:
        try:
            self.session.add(transaction)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def get_transactions(self, cnpj: str) -> list:
        return self.session.query(Transaction).filter(Transaction.estabelecimento == cnpj).all()

    def get_transactions_from_establishment_with_sum(self, cnpj: str) -> (list, Decimal):
        transactions = self.session.query(Transaction).filter(Transaction.estabelecimento == cnpj).all()
        _sum = self.session.query(func.sum(Transaction.valor)).filter(Transaction.estabelecimento == cnpj).scalar()
        return transactions, _sum
