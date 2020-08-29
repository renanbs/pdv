from http import HTTPStatus

from flask import Blueprint, jsonify

from injector import inject

from pdv.dependencies import Application


class EstablishmentsEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('EstablishmentsApp', __name__)

        @self.app.route('/api/v1/estabelecimento', methods=['POST'])
        def add_establishments():
            return jsonify({'aceito': True}), HTTPStatus.CREATED

        @self.app.route('/api/v1/estabelecimentos', methods=['GET'])
        def get_establishments():
            return jsonify({'aceito': True}), HTTPStatus.OK

        return app_bp
