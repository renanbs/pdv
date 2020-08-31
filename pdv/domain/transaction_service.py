from injector import inject

from pdv.config.dependencies import Session

from pdv.repository.transaction_interface import TransactionInterface
from pdv.repository.transaction_model import Transaction


class TransactionService(TransactionInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def create_transaction(self, name: str) -> None:
        tt = Transaction(name=name)
        self.session.add(tt)
        self.session.commit()
