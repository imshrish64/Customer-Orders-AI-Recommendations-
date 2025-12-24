def test_recommendations(client):
    # Create customer
    customer = client.post(
        "/customers/",
        json={"name": "Bob", "email": "bob@example.com"},
    ).json()

    # Create product
    product = client.post(
        "/products/",
        json={
            "name": "Laptop",
            "category": "Electronics",
            "price": 1200.0,
        },
    ).json()

    # Create order
    client.post(
        "/orders/",
        json={
            "customer_id": customer["id"],
            "product_id": product["id"],
            "quantity": 1,
            "price": 1200.0,
        },
    )

    # Call recommendations
    response = client.post(f"/customers/{customer['id']}/recommendations")

    assert response.status_code == 200

    data = response.json()
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)
