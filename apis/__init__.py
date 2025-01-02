from flask_restx import Api

from .hello import api as hello
from .student import api as student

api = Api(
    title="JobBoard",
    version="1.0",
    description="A simple job board API",
)

api.add_namespace(hello)
api.add_namespace(student)
