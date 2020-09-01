from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject

from pdv.config.dependencies import Application
from pdv.domain.transaction_helper import TransactionHelper
from pdv.domain.transaction_schema import TransactionSchema


class TransactionsEndpoint:

    @inject
    def __init__(self, app: Application, transaction_helper: TransactionHelper):
        self.app = app
        self.transaction_helper = transaction_helper

    def register_endpoints(self):
        app_bp = Blueprint('TransactionsApp', __name__)

        @self.app.route('/api/v1/transacao', methods=['POST'])
        def add_transaction():
            transaction = TransactionSchema().load(data=request.get_json())
            self.transaction_helper.create_transaction(transaction)
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/transacoes/estabelecimento', methods=['GET'])
        def get_transactions():
            return jsonify(self.transaction_helper.get_transactions_from_establishment('97064032000192')), HTTPStatus.OK

        return app_bp
