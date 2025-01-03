import pytest


def test_list_students(client):
    response = client.get("/students/")
    assert response.status_code == 200
    # assert response.json == {"message": "students!"}


def test_students(mongodb):
    assert "students" in mongodb.list_collection_names()
    manuel = mongodb.students.find_one({"name": "Sarah"})
    assert manuel["email"] == "sarah@nyu.edu"
