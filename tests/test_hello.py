import pytest


def test_hello(client):
    response = client.get("/hello/")
    assert response.status_code == 200
    assert response.json == {"hello": "world!"}
