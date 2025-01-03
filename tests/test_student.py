import pytest
import mongomock
from bson.json_util import dumps


def test_list_students(client, mongodb):
    response = client.get("/students/")
    assert response.status_code == 200
    assert response.json == dumps(mongodb.students.find())


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_student(client):
    response = client.get("students/sarah%40nyu.edu")
    assert response.status_code == 200
    assert response.json == {
        "name": "Sarah",
        "email": "sarah@nyu.edu",
        "seniority": "senior",
    }


def test_students(mongodb):
    assert "students" in mongodb.list_collection_names()
    manuel = mongodb.students.find_one({"name": "Sarah"})
    assert manuel["email"] == "sarah@nyu.edu"
