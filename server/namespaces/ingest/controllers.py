"""
"""
import sys
import logging
from datetime import datetime
from typing import Callable
from server.config.db import db
from .models import Temperature, DATA_TYPE_MAP, DBException

logger = logging.getLogger(__name__)


class InvalidData(Exception):
    """
    An exception representing invalid data
    """


def _get_data_object_factory(data_type: str) -> Callable:
    """
    Retrieves and returns the object factory associated with data_type; if 
    data_type is unsupported, InvalidData is raised
    Args:
        data_type: string data type
    Returns:
        Factory function
    Raises:
        InvalidData
    """
    this_module = sys.modules[__name__]
    factory_name = f"_{data_type}_factory"
    if hasattr(this_module, factory_name):
        return getattr(this_module, factory_name)

    raise InvalidData(f"{data_type} is an unsupported data type")


def _temperature_factory(data_item: dict) -> Temperature:
    """
    Factory function to create Temperature objects from the given data_item. If
    the data_item is not valid, InvalidData is raised
    Args:
        data_item: dictionary of values for a temperature reading
    Returns:
        an initialized Temperature object
    Raises:
        InvalidData
    """
    if None in [
        data_item.get(each_field) for each_field in
        [
            "sensor_type",
            "sensor_name",
            "temperature_scale",
            "temperature"
        ]
    ]:
        raise InvalidData(f"{data_item} is missing required fields")

    temperature_out = Temperature(
        **{x: data_item.get(x) for x in Temperature.all_fields}
    )

    return temperature_out


def post_data(data: list[dict], data_type: str):
    """
    Accepts list of data objects, validates, and saves them to the DB
    Args:
        data: list of data object dictionaries
        data_type: 
    Returns:
        None
    Raises:
        DBException
    """
    data_objects = []
    data_object_factory = _get_data_object_factory(data_type)
    for each_item in data:
        data_objects.append(data_object_factory(each_item))

    try:
        with db.session.begin():
            db.session.add_all(data_objects)
    except Exception as err:
        error_message = \
            f"Error {err.__class__.__name__} in db session for post_data: {err}"
        logger.error(error_message)
        raise DBException(error_message) from err


def get_data(
    data_type: str,
    page: int,
    page_size: int,
    start_date: str,
    end_date: str
) -> dict:
    """
    Return a page of data objects of type data_type, subject to optional
    start_date and end_date filters. If data_type is not supported, InvalidData
    is raised
    Args:
        data_type: string data type,
        page: integer page number,
        page_size: integer page size,
        start_date: start date string,
        end_date: end date string
    Returns:
        dictionary of results
    Raises:
        InvalidData
    """

    data_class = DATA_TYPE_MAP.get(data_type)
    if not data_class:
        raise InvalidData(f"{data_type} is not a supported data type")

    query = data_class.query

    if start_date:
        try:
            start_date = datetime.fromisoformat(start_date)
            query = query.filter(data_class.timestamp >= start_date)
        except ValueError as err:
            raise InvalidData(
                "Invalid start_date format. Use YYYY-MM-DD or ISO 8601."
            ) from err
    if end_date:
        try:
            end_date = datetime.fromisoformat(end_date)
            query = query.filter(data_class.timestamp <= end_date)
        except ValueError as err:
            raise InvalidData(
                "Invalid end_date format. Use YYYY-MM-DD or ISO 8601."
            ) from err

    paginated_results = query.paginate(
        page=page,
        per_page=page_size,
        error_out=False
    )
    results_out = [x.to_dict() for x in paginated_results.items]
    return {
        "data": results_out,
        "pagination": {
            "page": paginated_results.page,
            "per_page": paginated_results.per_page,
            "total": paginated_results.total,
            "pages": paginated_results.pages,
        }
    }
