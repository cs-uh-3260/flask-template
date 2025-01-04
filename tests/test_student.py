# Does the following test make sense?
# That is, it seems like something to make sure the test setup is working and not so much about testing the application.
# Good for sanity check, I guess?
def test_list_students(client):
    """
    Test that all seeded students are returned by the students/ endpoint.
    """
    # Call the list students API endpoint
    response = client.get("/students/")

    assert response.status_code == 200

    data = response.json
    assert isinstance(data, list)
    assert len(data) == 2  # We seeded two students in students.yaml

    # Validate content
    expected_students = [
        {"name": "Sarah", "email": "sarah@nyu.edu", "seniority": "senior"},
        {"name": "Manuel", "email": "manuel@nyu.edu", "seniority": "sophomore"},
    ]

    for student in expected_students:
        assert student in data


def test_get_existing_student(client):
    response = client.get("students/sarah@nyu.edu")
    assert response.status_code == 200
    assert response.json == {
        "name": "Sarah",
        "email": "sarah@nyu.edu",
        "seniority": "senior",
    }


def test_get_non_existing_student(client):
    response = client.get("students/non_existent@nyu.edu")
    assert response.status_code == 404
    assert response.json == "Student not found"


def test_students(seeded_student_db):
    assert "students" in seeded_student_db.list_collection_names()
    manuel = seeded_student_db.students.find_one({"name": "Sarah"})
    assert manuel["email"] == "sarah@nyu.edu"
