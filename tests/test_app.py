from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    # expect a dict of activities with required keys
    assert isinstance(data, dict)
    from fastapi.testclient import TestClient
    from src.app import app

    client = TestClient(app)


    def test_get_activities():
        resp = client.get("/activities")
        assert resp.status_code == 200
        data = resp.json()
        # expect a dict of activities with required keys
        assert isinstance(data, dict)
        assert "Chess Club" in data
        chess = data["Chess Club"]
        assert "participants" in chess


    def test_signup_and_remove_flow():
        activity = "Chess Club"
        test_email = "test_student@example.com"

        # Ensure this test email is not already present
        resp = client.get("/activities")
        assert resp.status_code == 200
        assert test_email not in resp.json()[activity]["participants"]

        # Sign up the new student
        resp = client.post(f"/activities/{activity}/signup?email={test_email}")
        assert resp.status_code == 200
        assert "Signed up" in resp.json().get("message", "")

        # Confirm participant was added
        resp = client.get("/activities")
        assert resp.status_code == 200
        assert test_email in resp.json()[activity]["participants"]

        # Duplicate signup should be rejected
        resp = client.post(f"/activities/{activity}/signup?email={test_email}")
        assert resp.status_code == 400

        # Now remove the participant
        resp = client.delete(f"/activities/{activity}/participants?email={test_email}")
        assert resp.status_code == 200
        assert "Removed" in resp.json().get("message", "")

        # Confirm participant removed
        resp = client.get("/activities")
        assert resp.status_code == 200
        assert test_email not in resp.json()[activity]["participants"]


    def test_remove_nonexistent_participant():
        activity = "Programming Class"
        missing_email = "not_in_list@example.com"

        # Ensure it's not present
        resp = client.get("/activities")
        assert resp.status_code == 200
        assert missing_email not in resp.json()[activity]["participants"]

        from fastapi.testclient import TestClient
        from src.app import app

        client = TestClient(app)


        def test_get_activities():
            resp = client.get("/activities")
            assert resp.status_code == 200
            data = resp.json()
            # expect a dict of activities with required keys
            assert isinstance(data, dict)
            assert "Chess Club" in data
            chess = data["Chess Club"]
            assert "participants" in chess


        def test_signup_and_remove_flow():
            activity = "Chess Club"
            test_email = "test_student@example.com"

            # Ensure this test email is not already present
            resp = client.get("/activities")
            assert resp.status_code == 200
            assert test_email not in resp.json()[activity]["participants"]

            # Sign up the new student
            resp = client.post(f"/activities/{activity}/signup?email={test_email}")
            assert resp.status_code == 200
            assert "Signed up" in resp.json().get("message", "")

            # Confirm participant was added
            resp = client.get("/activities")
            assert resp.status_code == 200
            assert test_email in resp.json()[activity]["participants"]

            # Duplicate signup should be rejected
            resp = client.post(f"/activities/{activity}/signup?email={test_email}")
            assert resp.status_code == 400

            # Now remove the participant
            resp = client.delete(f"/activities/{activity}/participants?email={test_email}")
            assert resp.status_code == 200
            assert "Removed" in resp.json().get("message", "")

            # Confirm participant removed
            resp = client.get("/activities")
            assert resp.status_code == 200
            assert test_email not in resp.json()[activity]["participants"]


        def test_remove_nonexistent_participant():
            activity = "Programming Class"
            missing_email = "not_in_list@example.com"

            # Ensure it's not present
            resp = client.get("/activities")
            assert resp.status_code == 200
            assert missing_email not in resp.json()[activity]["participants"]

            # Attempt to remove => 404
            resp = client.delete(f"/activities/{activity}/participants?email={missing_email}")
            assert resp.status_code == 404


        def test_signup_nonexistent_activity():
            resp = client.post("/activities/NoSuchActivity/signup?email=x@x.com")
            assert resp.status_code == 404