import pytest
import yaml
from app import create_app
from app.config import UnitTestConfig
from app.db.db import get_collection


@pytest.fixture(scope='session')
def app():
    app = create_app(UnitTestConfig)

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='session')
def student_fixture():
    """
    Load student data from the YAML fixture file.
    """
    with open("tests/unit/fixtures/students.yaml", "r") as file:
        students = yaml.safe_load(file)

    return students


@pytest.fixture(scope='function', autouse=True)
def seeded_student_db(student_fixture):
    """
    Preload the mock 'students' collection with data from the YAML fixture.
    """
    collection = get_collection("students")
    collection.delete_many({})  # Clear existing data
    collection.insert_many(student_fixture)
