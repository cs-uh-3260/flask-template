import pytest


def test_hello(client):
    response = client.get("/hello/")
    assert response.status_code == 200
    assert response.json == {"hello": "world!"}


def test_students(client):
    response = client.get("/students/")
    assert response.status_code == 200
    # assert response.json == {"message": "students!"}
