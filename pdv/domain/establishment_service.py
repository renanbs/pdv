from injector import inject

from pdv.domain.establishment_service_interface import EstablishmentServiceInterface
from pdv.repository.establishment_model import Establishment


class EstablishmentService:
    @inject
    def __init__(self, repository: EstablishmentServiceInterface):
        self.repository = repository

    def create_establishment(self, establishment: Establishment) -> None:
        self.repository.save(establishment)

    def get_establishments(self) -> list:
        return self.repository.list()

    def get_establishment(self, cnpj: str) -> Establishment:
        return self.repository.find_by_cnpj(cnpj)
