from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject
from marshmallow import ValidationError

from pdv.api.serializer import Serializer, SerializerException
from pdv.config.dependencies import Application
from pdv.domain.transaction_helper import TransactionHelper
from pdv.domain.transaction_schema import TransactionSchema
from pdv.repository.exceptions import RepositoryException


class TransactionsEndpoint:

    @inject
    def __init__(self, app: Application, transaction_helper: TransactionHelper):
        self.app = app
        self.transaction_helper = transaction_helper

    def register_endpoints(self):
        app_bp = Blueprint('TransactionsApp', __name__)

        @self.app.route('/api/v1/transacao', methods=['POST'])
        def add_transaction():
            try:
                transaction = TransactionSchema().load(data=request.get_json())
                self.transaction_helper.create_transaction(transaction)
            except (RepositoryException, ValueError, ValidationError):
                return {'aceito': False}, HTTPStatus.BAD_REQUEST

            return {'aceito': True}, HTTPStatus.CREATED

        @self.app.route('/api/v1/transacoes/estabelecimento', methods=['GET'])
        def get_transactions():
            try:
                serializer = Serializer(request.args.get('cnpj'))
                serializer.is_valid()
            except SerializerException as ex:
                return {'error': str(ex)}, HTTPStatus.BAD_REQUEST

            return jsonify(self.transaction_helper.get_transactions_from_establishment(serializer.cnpj)), HTTPStatus.OK

        return app_bp
