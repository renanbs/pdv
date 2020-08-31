from http import HTTPStatus

from flask import Blueprint, jsonify

from injector import inject

from pdv.config.dependencies import Application
from pdv.repository.establishment_interface import EstablishmentInterface
from pdv.repository.transaction_interface import TransactionInterface


class EstablishmentsEndpoint:

    @inject
    def __init__(self, app: Application, ec: EstablishmentInterface, transaction_service: TransactionInterface):
        self.app = app
        self.ec = ec
        self.transaction_service = transaction_service

    def register_endpoints(self):
        app_bp = Blueprint('EstablishmentsApp', __name__)

        @self.app.route('/api/v1/estabelecimento', methods=['POST'])
        def add_establishments():
            self.ec.create_establishment('my ec')
            self.transaction_service.create_transaction('my transaction')

            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/estabelecimentos', methods=['GET'])
        def get_establishments():
            return jsonify({'aceito': True}), HTTPStatus.OK

        return app_bp
