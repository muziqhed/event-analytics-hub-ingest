import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS", "True"
).lower() == "true"
DEVELOPMENT = os.environ.get(
    "SQLALCHEMY_DEVELOPMENT", "False"
).lower() == "true"
DEBUG = os.environ.get(
    "SQLALCHEMY_DEBUG", "False"
).lower() == "true"
SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URL")


class DBConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
    DEVELOPMENT = DEVELOPMENT
    DEBUG = DEBUG
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI 

    