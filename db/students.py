from .db import get_db

# collection name
STUDENT_COLLECTION = "students"

# fields
ID = "_id"
NAME = "name"
EMAIL = "email"
SENIORITY = "seniority"


def _get_student_collection():
    db = get_db()
    return db[STUDENT_COLLECTION]


def get_students():
    students = _get_student_collection().find({})
    return students


def create_student(name: str, email: str, seniority: str):
    student = {NAME: name, EMAIL: email, SENIORITY: seniority}
    result = _get_student_collection().insert_one(student)
    return result.inserted_id


def update_student(lookupemail: str, name: str, email: str, seniority: str):
    student_record = get_student_by_email(lookupemail)

    if student_record is None:
        return None

    new_data = {NAME: name, EMAIL: email, SENIORITY: seniority}
    result = _get_student_collection().update_one(student_record, {"$set": new_data})

    return result


def get_student_by_email(email: str):
    student = _get_student_collection().find_one({EMAIL: email})
    return student
