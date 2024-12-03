from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
from tasks import Task


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_get_task_by_id():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Buy milk"


def test_add_and_expect_one_more_than_before():
    def count():
        response = client.get("/tasks")
        return len(response.json())

    c1 = count()
    res = client.post("/tasks", json={"title": "Buy milk", "category": "shopping"})
    assert count() == c1 + 1
    Task(**res.json())