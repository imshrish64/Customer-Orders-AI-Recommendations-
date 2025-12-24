def test_create_order(client):
    # Create customer
    customer = client.post(
        "/customers/",
        json={"name": "Alice", "email": "alice@example.com"},
    ).json()

    # Create product
    product = client.post(
        "/products/",
        json={
            "name": "Mouse",
            "category": "Electronics",
            "price": 25.0,
        },
    ).json()

    # Create order
    response = client.post(
        "/orders/",
        json={
            "customer_id": customer["id"],
            "product_id": product["id"],
            "quantity": 2,
            "price": 25.0,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == customer["id"]
    assert data["product_id"] == product["id"]
