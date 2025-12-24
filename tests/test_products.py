def test_create_product(client):
    response = client.post(
        "/products/",
        json={
            "name": "Laptop",
            "category": "Electronics",
            "price": 1200.0,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) >= 1
