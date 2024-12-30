"""
"""
from flask import Blueprint, Flask

#from server.config.db import db_connect
from server.config.namespaces import SERVICE_BASE_URL, namespace_init


def create_flask_app() -> Flask:
    base_app = Flask(__name__)
    blueprint = Blueprint("api", __name__, url_prefix=SERVICE_BASE_URL)
    namespace_init(blueprint)
    base_app.register_blueprint(blueprint)
    return base_app


def init_app() -> Flask:
    app = create_flask_app()
#    db_connect()
    return app
