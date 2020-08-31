from injector import inject

from pdv.repository.establishment_repository import EstablishmentRepository


class EstablishmentService:
    @inject
    def __init__(self, repository: EstablishmentRepository):
        self.repository = repository

    def create_establishment(self, name: str):
        self.repository.save(name)
