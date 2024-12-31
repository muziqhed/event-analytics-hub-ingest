"""
Tests for main namespace
"""
from http import HTTPStatus
from server.config.namespaces import SERVICE_BASE_URL


def test_health_endpoint(app_client):
    """Test health endpoint GET"""
    response = app_client.get(f"{SERVICE_BASE_URL}/main/health")
    assert response.status_code == HTTPStatus.OK
