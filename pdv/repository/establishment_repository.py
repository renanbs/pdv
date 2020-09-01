from injector import inject

from pdv.config.dependencies import Session
from pdv.domain.establishment_service_interface import EstablishmentServiceInterface
from pdv.repository.establishment_model import Establishment
from pdv.repository.exceptions import RepositoryException


class EstablishmentServiceRepository(EstablishmentServiceInterface):
    @inject
    def __init__(self, session: Session):
        self.session = session

    def save(self, establishment: Establishment) -> None:
        try:
            self.session.add(establishment)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositoryException(e)

    def find_by_cnpj(self, cnpj: str) -> Establishment:
        try:
            return self.session.query(Establishment).filter(Establishment.cnpj == cnpj).one()
        except Exception as e:
            raise RepositoryException(e)

    def list(self) -> list:
        try:
            return self.session.query(Establishment).all()
        except Exception as e:
            raise RepositoryException(e)
