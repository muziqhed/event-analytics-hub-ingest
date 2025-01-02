"""
"""
import pytest
from sqlalchemy.sql import text
from tests.fixtures.ingest_fixtures import TEST_GOOD_TEMP_DATA
from server.app import init_app
from server.namespaces.ingest.models import Temperature
from server.config.db import db


@pytest.fixture()
def app():
    """
    """
    app = init_app()
    app.config["TESTING"] = True
    app.config.update(dict(WTF_CSRF_ENABLED=False))
    yield app


@pytest.fixture()
def app_client(app):
    """"""
    return app.test_client()


@pytest.fixture()
def mock_good_temp_data(app):
    """
    Sets the DB up with TEST_GOOD_TEMP_DATA
    """
    with app.app_context():
        db.session.add_all([Temperature(**x) for x in TEST_GOOD_TEMP_DATA])
        db.session.commit()


@pytest.fixture()
def cleanup_database(app):
    """
    A fixture that ensures the database is cleaned up after each test.
    This fixture runs automatically for each test.
    """
    yield  # Run the test
    with app.app_context():
        db.session.rollback()
        db.session.execute(
            text("TRUNCATE TABLE temperature RESTART IDENTITY CASCADE")
        )
        db.session.commit()
