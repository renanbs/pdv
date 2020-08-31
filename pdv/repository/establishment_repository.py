from injector import inject

from pdv.config.dependencies import Session
from pdv.domain.establishment_interface import EstablishmentInterface
from pdv.repository.establishment_model import Establishment


class EstablishmentRepository(EstablishmentInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def save(self, name: str) -> None:
        ec = Establishment(name=name)
        self.session.add(ec)
        self.session.commit()
