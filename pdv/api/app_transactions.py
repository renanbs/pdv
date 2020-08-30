from http import HTTPStatus

from flask import Blueprint, jsonify

from injector import inject

from pdv.config.dependencies import Application


class TransactionsEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('TransactionApp', __name__)

        @self.app.route('/api/v1/transacao', methods=['POST'])
        def add_transaction():
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/transacoes/estabelecimento', methods=['GET'])
        def get_transaction():
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        return app_bp
