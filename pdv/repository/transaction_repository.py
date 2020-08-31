from injector import inject

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
