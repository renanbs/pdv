.PHONY: test all
.DEFAULT_GOAL := default_target

PROJECT_NAME := pdv
PYTHON_VERSION := 3.8.5
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

setup-dev:
	pip install pip --upgrade
	pip install -U setuptools wheel==0.35.1
	pip install -r requirements-dev.txt

test:
	pytest -v --cov=pdv --ignore=pdv/repository/alembic --cov-fail-under=80

test-coverage:
	pytest -v --cov=pdv --cov-report=term-missing --cov-report=html --ignore=pdv/repository/alembic --cov-fail-under=80

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

pycodestyle:
	echo "Running pycodestyle"
	pycodestyle

flake8:
	echo "Running flake8"
	flake8

code-convention: pycodestyle flake8

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/
	rm -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

all : setup-dev test-coverage code-convention

default_target: code-convention test

setup-db:
	alembic upgrade head

run:
	flask run

build-docker:
	docker build -t pdv .

run-docker:
	docker run --name my-pdv-server -p 5000:5000 pdv
