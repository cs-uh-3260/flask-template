from flask_restx import Namespace, Resource
from db.students import create as create_student

api = Namespace(
    "student", description="Student endpoints for getting and creating students"
)


@api.route("/student")
class Student(Resource):

    @api.response(HTTPStatus.OK, "Success")
    @api.response(HTTPStatus.NOT_ACCEPTABLE, "Not acceptable")
    @api.expect(PEOPLE_CREATE_FLDS)
    def put(self, name: str, seniority: str):
        id = create_student(name, seniority)
        print(f"Created student with id: {id}")
