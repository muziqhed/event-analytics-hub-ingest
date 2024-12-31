"""
"""
import logging
from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource, fields
from .controllers import post_data, get_data, InvalidData

logger = logging.getLogger(__name__)
ingest_ns = Namespace('ingest', description="Data ingest")
data_submission_schema = ingest_ns.model(
    "Data Submission Payload",
    {"data": fields.List(fields.Raw, required=True)}
)
data_item_schema = {
    "id": fields.String,
    "timestamp": fields.String,
    "is_validated": fields.Boolean,
    "*": fields.Wildcard(fields.String)
}

data_paginated_schema = {
    "data": fields.List(fields.Nested(data_item_schema)),
    "*": fields.Wildcard(fields.Raw)

}


@ingest_ns.route('/data/<string:data_type>')
class DataIngest(Resource):
    """
    Data route definitions
    """
    @ingest_ns.response(HTTPStatus.BAD_REQUEST, "Bad Request")
    @ingest_ns.response(HTTPStatus.METHOD_NOT_ALLOWED, "Method Not Allowed")
    @ingest_ns.response(HTTPStatus.OK, "Data Successfully Retrieved")
    @ingest_ns.marshal_with(data_paginated_schema)
    def get(self, data_type: str):
        try:
            page = request.args.get("page", default=1, type=int)
            page_size = request.args.get("page_size", default=10, type=int)
            start_date = request.args.get("start_date")
            end_date = request.args.get("end_date")
            response_payload = get_data(
                data_type,
                page,
                page_size,
                start_date,
                end_date
            )
            return response_payload, HTTPStatus.OK

        except InvalidData as err:
            logging.error(str(err))
            ingest_ns.abort(HTTPStatus.BAD_REQUEST, err)
        except Exception as err:
            logging.error(str(err))
            ingest_ns.abort(HTTPStatus.INTERNAL_SERVER_ERROR, err)

    @ingest_ns.response(HTTPStatus.BAD_REQUEST, "Bad Request")
    @ingest_ns.response(HTTPStatus.METHOD_NOT_ALLOWED, "Method Not Allowed")
    @ingest_ns.response(HTTPStatus.CREATED, "Data Successfully Submitted")
    @ingest_ns.expect(data_submission_schema, validate=True)
    def post(self, data_type: str):
        try:
            data = ingest_ns.payload.get("data")
            post_data(data, data_type)
            return "Success", HTTPStatus.CREATED

        except InvalidData as err:
            logging.error(str(err))
            ingest_ns.abort(HTTPStatus.BAD_REQUEST, err)
        except Exception as err:
            logging.error(str(err))
            ingest_ns.abort(HTTPStatus.INTERNAL_SERVER_ERROR, err)
