"""
"""
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource

main_ns = Namespace('main', description="main")


@main_ns.route('/health')
class Health(Resource):
    @main_ns.response(HTTPStatus.OK.value, "API Health Endpoint")
    def get(self):
        return Response('Health GET request successful', mimetype="application/json", status=200)
