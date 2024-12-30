"""
"""
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource

ingest_ns = Namespace('ingest', description="Data ingest")


@ingest_ns.route('/data')
class DataIngest(Resource):
    @ingest_ns.response(HTTPStatus.OK.value, "Data Successfully Submitted")
    def post(self):
        return Response('Ingest POST request successful', mimetype="application/json", status=200)
    