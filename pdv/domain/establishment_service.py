from injector import inject

from pdv.repository.establishment_model import Establishment
from pdv.repository.establishment_repository import EstablishmentServiceRepository


class EstablishmentService:
    @inject
    def __init__(self, repository: EstablishmentServiceRepository):
        self.repository = repository

    def create_establishment(self, establishment: Establishment) -> None:
        self.repository.save(establishment)

    def get_establishments(self):
        return self.repository.list()
