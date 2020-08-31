from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject

from pdv.config.dependencies import Application
from pdv.domain.transaction_schema import TransactionSchema
from pdv.domain.transaction_service import TransactionService


class TransactionsEndpoint:

    @inject
    def __init__(self, app: Application, transaction_service: TransactionService):
        self.app = app
        self.transaction_service = transaction_service

    def register_endpoints(self):
        app_bp = Blueprint('TransactionsApp', __name__)

        @self.app.route('/api/v1/transacao', methods=['POST'])
        def add_transaction():
            transaction = TransactionSchema().load(data=request.get_json())
            self.transaction_service.create_transaction(transaction)
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/transacoes/estabelecimento', methods=['GET'])
        def get_transaction():
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        return app_bp
