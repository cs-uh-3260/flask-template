import pytest


def test_list_students(client):
    response = client.get("/students/")
    assert response.status_code == 200
    # assert response.json == {"message": "students!"}
