from flask_restx import Api

from .hello import api as hello

api = Api(
    title="My Title",
    version="1.0",
    description="A description",
    # All API metadatas
)

api.add_namespace(hello)
