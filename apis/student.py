from flask_restx import Namespace, Resource, fields
import db.students as students
from http import HTTPStatus
from flask import request
from bson.json_util import dumps

api = Namespace("students", description="Endpoint for students")

STUDENT_CREATE_FLDS = api.model(
    "AddNewStudentEntry",
    {
        students.NAME: fields.String,
        students.EMAIL: fields.String,
        students.SENIORITY: fields.String,
    },
)


@api.route("/")
class StudentList(Resource):

    def get(self):
        student_list = students.get_students()
        return dumps(student_list), HTTPStatus.OK

    @api.expect(STUDENT_CREATE_FLDS)
    def post(self):
        name = request.json.get(students.NAME)
        seniority = request.json.get(students.SENIORITY)
        email = request.json.get(students.EMAIL)
        student_id = students.create_student(name, email, seniority)
        print(f"Created student with id: {student_id}")
        return "Student created", HTTPStatus.OK


@api.route("/<email>")
@api.param("email", "Student email to use for lookup")
@api.response(404, "Student not found")
@api.response(HTTPStatus.OK, "Success")
@api.response(HTTPStatus.NOT_ACCEPTABLE, "Not acceptable")
class Student(Resource):

    @api.doc("Get a specific student, identified by email")
    def get(self, email):
        student = students.get_student_by_email(email)

        if student is None:
            return "Student not found", HTTPStatus.NOT_FOUND

        return dumps(student), HTTPStatus.OK

    @api.expect(STUDENT_CREATE_FLDS)
    @api.doc("Update a specific student, identified by email")
    def put(self, email):

        name = request.json.get(students.NAME)
        seniority = request.json.get(students.SENIORITY)
        new_email = request.json.get(students.EMAIL)

        updated_student = students.update_student(email, name, new_email, seniority)

        if updated_student is None:
            return "Student not found", HTTPStatus.NOT_FOUND

        return "Student updated", HTTPStatus.OK
