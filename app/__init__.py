from flask import Flask

from app.config import DevelopmentConfig
from .apis.student import api as student
from .apis.hello import api as hello
from flask_restx import Api


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(
        title="JobBoard",
        version="1.0",
        description="A simple job board API",
    )

    api.init_app(app)

    api.add_namespace(hello)
    api.add_namespace(student)

    return app
