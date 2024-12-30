"""
"""
import pytest
from server.app import create_flask_app

@pytest.fixture()
def app():
    """"""
    app = create_flask_app()
    app.config["TESTING"] = True
    app.config.update(dict(WTF_CSRF_ENABLED=False))
    #create mocked db connection
    yield app


@pytest.fixture()
def app_client(app):
    """"""
    return app.test_client()