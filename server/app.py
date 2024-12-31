"""
"""
from flask import Blueprint, Flask
from server.config.namespaces import SERVICE_BASE_URL, namespace_init
from server.config.db import DBConfig, db, migrate


def create_flask_app() -> Flask:
    base_app = Flask(__name__)
    blueprint = Blueprint("api", __name__, url_prefix=SERVICE_BASE_URL)
    namespace_init(blueprint)
    base_app.register_blueprint(blueprint)
    return base_app


def init_app() -> Flask:
    app = create_flask_app()
    app.config.from_object(DBConfig)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    return app
