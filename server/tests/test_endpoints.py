from http.client import (
    BAD_REQUEST,
    FORBIDDEN,
    NOT_ACCEPTABLE,
    NOT_FOUND,
    OK,
    SERVICE_UNAVAILABLE,
)

from unittest.mock import patch

import pytest

from data.people import NAME

import server.app as endpoint

TEST_CLIENT = endpoint.app.test_client()


def test_hello():
    resp = TEST_CLIENT.get("/hello")
    resp_json = resp.get_json()
    assert "Hello World!" in resp_json
