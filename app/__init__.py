from flask import Flask
from .apis.student import api as student
from .apis.hello import api as hello
from flask_restx import Api


def create_app():
    app = Flask(__name__)

    api = Api(
        title="JobBoard",
        version="1.0",
        description="A simple job board API",
    )

    api.init_app(app)

    api.add_namespace(hello)
    api.add_namespace(student)

    return app
