from http import HTTPStatus

import pytest


@pytest.fixture
def ec():
    return {
        'nome': 'Ec do Juca',
        'cnpj': '97064032000192',
        'dono': 'Juca da Silva',
        'telefone': '51999999999'
    }


def test_should_get_establishments(api_client):
    response = api_client.get('/api/v1/estabelecimentos')
    assert response.status_code == HTTPStatus.OK


def test_should_create_establishment(api_client, mocker, ec):
    mocker.patch('pdv.domain.establishment_service.EstablishmentService.create_establishment')

    response = api_client.post('/api/v1/estabelecimento', json=ec)
    assert response.status_code == HTTPStatus.CREATED


def test_should_not_create_establishment_with_invalid_cnpj(api_client, ec):
    ec['cnpj'] = '123456789'

    response = api_client.post('/api/v1/estabelecimento', json=ec)
    assert response.status_code == HTTPStatus.BAD_REQUEST
