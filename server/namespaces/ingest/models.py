"""
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from server.config.db import db


class DBException(Exception):
    """
    Class representing a database or model-related error
    """


class Temperature(db.Model):
    """
    Temperature data class
    """
    __tablename__ = "temperature"
    all_fields = [
        "id",
        "sensor_type",
        "sensor_name",
        "temperature_scale",
        "temperature",
        "timestamp",
        "is_validated"
    ]

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=db.text("gen_random_uuid()"),
        unique=True,
        nullable=False
    )
    sensor_type = db.Column(db.String(120), nullable=False)
    sensor_name = db.Column(db.String(120), nullable=False)
    temperature_scale = db.Column(
        db.Enum("celsius", "fahrenheit", name="temperature_scale_enum")
    )
    temperature = db.Column(db.Float(), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    is_validated = db.Column(db.Boolean(), default=False)

    def to_dict(self, include_fields=None):
        """
        Map object to dictionary
        """
        include = include_fields or self.all_fields

        return {
            field: getattr(self, field) for field in include
            if hasattr(self, field)
        }

    def __repr__(self):
        return f"<Temperature {self.__class__.__name__}>"


DATA_TYPE_MAP = {x.__tablename__: x for x in [Temperature]}
