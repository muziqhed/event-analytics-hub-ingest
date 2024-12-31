"""
Tests for ingest namespace
"""
from http import HTTPStatus
from server.config.namespaces import SERVICE_BASE_URL
from tests.fixtures.ingest_fixtures import (
    TEST_GOOD_TEMP_DATA, TEST_BAD_TEMP_DATA
)


def test_post_data_succcess(app_client, cleanup_database):
    """
    Test sucessful post
    """
    response = app_client.post(
        f"{SERVICE_BASE_URL}/ingest/data/temperature",
        json={"data": TEST_GOOD_TEMP_DATA}
    )
    assert response.status_code == HTTPStatus.CREATED


def test_get_filtered_data_success(
    app_client,
    mock_good_temp_data,
    cleanup_database
):
    """
    Test get filtered data
    """
    response = app_client.get(
        f"{SERVICE_BASE_URL}/ingest/data/temperature?" +
        "start_date=2024-01-01T12:00:05&end_date=2024-01-01T12:00:12",
    )
    assert response.status_code == HTTPStatus.OK
    assert len(response.json["data"]) == 2
    assert response.json["pagination"] == {
        "page": 1,
        "pages": 1,
        "per_page": 10,
        "total": 2
    }


def test_post_data_fail_bad_fields(app_client):
    """
    Test failure on missing or bad fields
    """
    response = app_client.post(
        f"{SERVICE_BASE_URL}/ingest/data/temperature",
        json={"data": TEST_BAD_TEMP_DATA}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "missing required fields" in response.json.get("message", "")


def test_post_data_fail_bad_values(app_client):
    """
    Test failure on incorrect data field types
    """
    response = app_client.post(
        f"{SERVICE_BASE_URL}/ingest/data/temperature",
        json={
            "data": [
                {
                    "sensor_type": True,
                    "sensor_name": 100,
                    "temperature_scale": "badstring",
                    "temperature": "32",
                    "timestamp": "2024-01-01"
                }
            ]
        }
    )
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert "DataError" in response.json.get("message", "")


def test_post_data_fail_bad_request(app_client):
    """
    Test failure on bad request payload structure
    """
    response = app_client.post(
        f"{SERVICE_BASE_URL}/ingest/data/temperature",
        json={"wrong_top_level_key": "bad_data"}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "Input payload validation failed" in response.json.get(
        "message", "")


def test_post_data_fail_bad_data_type(app_client):
    """
    Test failure on bad data type
    """
    response = app_client.post(
        f"{SERVICE_BASE_URL}/ingest/data/unsupported_type",
        json={"data": TEST_GOOD_TEMP_DATA}
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "is an unsupported data type" in response.json.get("message", "")
