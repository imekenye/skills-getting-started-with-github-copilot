from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_signup_and_remove_flow():
    activity = "Chess Club"
    test_email = "clean_test_student@example.com"

    # Ensure this test email is not already present
    resp = client.get("/activities")
    assert resp.status_code == 200
    assert test_email not in resp.json()[activity]["participants"]

    # Sign up the new student
    resp = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert resp.status_code == 200

    # Confirm participant was added
    resp = client.get("/activities")
    assert test_email in resp.json()[activity]["participants"]

    # Duplicate signup should be rejected
    resp = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert resp.status_code == 400

    # Now remove the participant
    resp = client.delete(f"/activities/{activity}/participants?email={test_email}")
    assert resp.status_code == 200

    # Confirm participant removed
    resp = client.get("/activities")
    assert test_email not in resp.json()[activity]["participants"]


def test_remove_nonexistent_participant():
    activity = "Programming Class"
    missing_email = "not_in_list_clean@example.com"

    resp = client.get("/activities")
    assert resp.status_code == 200
    assert missing_email not in resp.json()[activity]["participants"]

    resp = client.delete(f"/activities/{activity}/participants?email={missing_email}")
    assert resp.status_code == 404


def test_signup_nonexistent_activity():
    resp = client.post("/activities/NoSuchActivity/signup?email=x@x.com")
    assert resp.status_code == 404
