from http import HTTPStatus

import pytest


def test_should_not_get_transactions_without_cnpj(api_client):
    response = api_client.get('/api/v1/transacoes/estabelecimento')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'cnpj filter is required'}


def test_should_not_get_transactions_with_invalid_cnpj(api_client):
    response = api_client.get('/api/v1/transacoes/estabelecimento?cnpj=125-4874')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'error': 'invalid cnpj'}


def test_should_get_transactions(api_client, mocker):
    return_value = {'transactions': 'my_transactions'}
    mocker.patch('pdv.domain.transaction_helper.TransactionHelper.get_transactions_from_establishment',
                 return_value=return_value)
    response = api_client.get('/api/v1/transacoes/estabelecimento?cnpj=97064032000192')

    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == return_value


@pytest.fixture
def valid_transaction():
    return {
        'cliente': '48508866046',
        'descricao': 'my description',
        'estabelecimento': '97064032000192',
        'valor': 112
    }


def test_should_create_transaction(api_client, valid_transaction, mocker):
    mocker.patch('pdv.domain.transaction_helper.TransactionHelper.create_transaction')
    response = api_client.post('/api/v1/transacao', json=valid_transaction)

    assert response.status_code == HTTPStatus.CREATED
    assert response.get_json() == {'aceito': True}


@pytest.mark.parametrize('key, value', [('cliente', '01235896'), ('estabelecimento', '5645645'), ('valor', '3+8')])
def test_should_not_create_transaction_with_invalid_data(api_client, valid_transaction, key, value):
    valid_transaction[key] = value
    response = api_client.post('/api/v1/transacao', json=valid_transaction)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json() == {'aceito': False}
