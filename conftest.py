from unittest.mock import MagicMock

import pytest

from injector import Injector, InstanceProvider

from pdv.config.main_module import MODULES
from pdv.domain.establishment_service import EstablishmentService
from pdv.repository.establishment_repository import EstablishmentServiceRepository


@pytest.fixture
def injector(establishment_service):
    injector = Injector(MODULES)
    injector.binder.bind(EstablishmentService, to=InstanceProvider(establishment_service))
    yield injector


@pytest.fixture
def establishment_service(establishment_service_repository):
    return EstablishmentService(establishment_service_repository)


@pytest.fixture
def establishment_service_repository():
    return EstablishmentServiceRepository(MagicMock())
