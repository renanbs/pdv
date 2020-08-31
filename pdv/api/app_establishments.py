from http import HTTPStatus

from flask import Blueprint, jsonify

from injector import inject

from pdv.config.dependencies import Application


from pdv.domain.establishment_service import EstablishmentService
from pdv.domain.transaction_service import TransactionService


class EstablishmentsEndpoint:

    @inject
    def __init__(self, app: Application, ec_service: EstablishmentService, transaction_service: TransactionService):
        self.app = app
        self.ec_service = ec_service
        self.transaction_service = transaction_service

    def register_endpoints(self):
        app_bp = Blueprint('EstablishmentsApp', __name__)

        @self.app.route('/api/v1/estabelecimento', methods=['POST'])
        def add_establishments():
            self.ec_service.create_establishment('my ec 2')
            self.transaction_service.create_transaction('my transaction 2')

            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/estabelecimentos', methods=['GET'])
        def get_establishments():
            return jsonify({'aceito': True}), HTTPStatus.OK

        return app_bp
