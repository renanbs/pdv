from unittest.mock import MagicMock

import pytest

from injector import Injector

from pdv.config.dependencies import DBEngine, Session
from pdv.config.main_module import MODULES


@pytest.fixture
def engine():
    return MagicMock()


@pytest.fixture
def session():
    return MagicMock()


@pytest.fixture
def injector(engine, session):
    injector = Injector(MODULES)
    injector.binder.bind(DBEngine, to=engine)
    injector.binder.bind(Session, to=session)

    yield injector
