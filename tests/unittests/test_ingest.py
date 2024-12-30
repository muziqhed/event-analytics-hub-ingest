"""
Tests for ingest namespace
"""
from http import HTTPStatus
from server.config.namespaces import SERVICE_BASE_URL


def test_post_data(app_client):
    """Test health endpoint GET"""
    response = app_client.post(f"{SERVICE_BASE_URL}/ingest/data")
    assert response.status_code == HTTPStatus.OK
