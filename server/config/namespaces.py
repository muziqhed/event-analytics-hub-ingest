from flask import Blueprint, Flask
from flask_restx import Api, apidoc

from server.namespaces import (
    main_ns,
    ingest
)

SERVICE_BASE_URL = "/api/ea-hub-ingest"


class EAHubIngestApi(Api):
    def _register_apidoc(self, app: Flask) -> None:
        conf = app.extensions.setdefault("restx", {})
        if not conf.get("apidoc_registered", False):
            app.register_blueprint(apidoc.apidoc, url_prefix=SERVICE_BASE_URL)
        conf["apidoc_registered"] = True


def namespace_init(blueprint: Blueprint) -> None:
    """Adds all projects namespaces to the API"""
    api = EAHubIngestApi(
        blueprint,
        version="1.0",
        title="Event Analytics Hub Ingest API",
        description="API description goes here",
    )
    api.add_namespace(main_ns)
    api.add_namespace(ingest.ingest_ns)
