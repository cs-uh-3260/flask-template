from flask_restx import Namespace, Resource
from http import HTTPStatus

api = Namespace(
    "hello", description="Simple hello world endpoint for making sure app works"
)


@api.route("/")
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """

    def get(self):
        """
        A trivial endpoint to see if the server is running.
        """
        return {"hello": "world!"}, HTTPStatus.OK
