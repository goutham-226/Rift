from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.main import app, reset

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_store() -> Iterator[None]:
    reset()
    yield


def test_list_starts_empty() -> None:
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item() -> None:
    response = client.post("/items", json={"name": "widget", "price": 9.99})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "widget"
    assert body["price"] == 9.99


def test_get_item_by_id() -> None:
    client.post("/items", json={"name": "widget", "price": 9.99})
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "widget", "price": 9.99}


def test_missing_item_is_404() -> None:
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
