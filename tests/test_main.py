from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "price": 10.5, "description": "A test item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.5
    assert "id" in data 

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item():
    # First, create an item to ensure it exists
    response = client.post("/items/", json={"name": "Item to Read", "price": 1.0})
    item_id = response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Item to Read"
    assert data["id"] == item_id

def test_read_nonexistent_item():
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_update_item():
    # First, create an item to update
    response = client.post("/items/", json={"name": "Item to Update", "price": 2.0})
    item_id = response.json()["id"]

    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Item", "price": 3.0, "description": "Updated desc"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item"
    assert data["price"] == 3.0
    assert data["description"] == "Updated desc"

def test_delete_item():
    # First, create an item to delete
    response = client.post("/items/", json={"name": "Item to Delete", "price": 4.0})
    item_id = response.json()["id"]

    # Delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200

    # Verify it's gone
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404