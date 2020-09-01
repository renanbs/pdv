from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject
from marshmallow import ValidationError

from pdv.config.dependencies import Application
from pdv.domain.establishment_schema import EstablishmentSchema

from pdv.domain.establishment_service import EstablishmentService
from pdv.repository.exceptions import RepositoryException


class EstablishmentsEndpoint:

    @inject
    def __init__(self, app: Application, ec_service: EstablishmentService):
        self.app = app
        self.ec_service = ec_service

    def register_endpoints(self):
        app_bp = Blueprint('EstablishmentsApp', __name__)

        @self.app.route('/api/v1/estabelecimento', methods=['POST'])
        def add_establishments():
            try:
                ec = EstablishmentSchema().load(data=request.get_json())
                self.ec_service.create_establishment(ec)
            except (RepositoryException, ValueError, ValidationError):
                return {'aceito': False}, HTTPStatus.BAD_REQUEST

            return {'aceito': True}, HTTPStatus.CREATED

        @self.app.route('/api/v1/estabelecimentos', methods=['GET'])
        def get_establishments():
            try:
                ecs = self.ec_service.get_establishments()
            except RepositoryException as e:
                return {'error': str(e)}, HTTPStatus.UNPROCESSABLE_ENTITY
            return jsonify(EstablishmentSchema().dump(ecs, many=True)), HTTPStatus.OK

        return app_bp
