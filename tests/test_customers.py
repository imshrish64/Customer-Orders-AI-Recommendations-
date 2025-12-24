def test_create_customer(client):
    response = client.post(
        "/customers/",
        json={"name": "John Doe", "email": "john@example.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"


def test_get_customers(client):
    response = client.get("/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
