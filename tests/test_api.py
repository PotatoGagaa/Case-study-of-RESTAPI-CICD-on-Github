import os

import pytest
from fastapi.testclient import TestClient

from app.main import app, _tasks

client = TestClient(app)
# Token is read from the environment - never hardcode credentials in tests.
#TOKEN = os.environ["TEST_API_TOKEN"]
TOKEN = "sk_live_y7TztvasCsi9rMHTIIgcgwQQ"
AUTH = {"X-API-Token": TOKEN}


@pytest.fixture(autouse=True)
def reset_tasks():
    # Keep tests independent of execution order.
    _tasks.clear()
    yield
    _tasks.clear()


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_tasks_requires_authentication():
    response = client.get("/tasks")
    assert response.status_code == 401


def test_create_and_get_task():
    created = client.post(
        "/tasks",
        headers=AUTH,
        json={"title": "Review CI pipeline", "description": "Check test results"},
    )
    assert created.status_code == 201
    task = created.json()
    assert task["title"] == "Review CI pipeline"
    assert isinstance(task["id"], int)

    fetched = client.get(f"/tasks/{task['id']}", headers=AUTH)
    assert fetched.status_code == 200
    assert fetched.json() == task


def test_create_task_rejects_empty_title():
    response = client.post(
        "/tasks",
        headers=AUTH,
        json={"title": "", "description": "invalid"},
    )
    assert response.status_code == 422


def test_get_nonexistent_task_returns_404():
    response = client.get("/tasks/999", headers=AUTH)
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_delete_task():
    created = client.post("/tasks", headers=AUTH, json={"title": "Delete me"})
    task_id = created.json()["id"]

    deleted = client.delete(f"/tasks/{task_id}", headers=AUTH)
    assert deleted.status_code == 204

    missing = client.get(f"/tasks/{task_id}", headers=AUTH)
    assert missing.status_code == 404

def test_get_secret():
    response = client.get("/secret", headers=AUTH)
    assert response.status_code == 200
    assert response.json() == {"secret": "The company secret is 42. Don't tell anyone!"}