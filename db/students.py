from db import get_db

# collection name
STUDENT_COLLECTION = "students"

# fields
ID = "_id"
NAME = "name"
SENIORITY = "seniority"


def _get_student_collection():
    db = get_db()
    return db[STUDENT_COLLECTION]


def get_students():
    students = _get_student_collection().find()
    return list(students)


def create(name: str, seniority: str):
    student = {NAME: name, SENIORITY: seniority}
    id = _get_student_collection().insert_one(student)
    return id
