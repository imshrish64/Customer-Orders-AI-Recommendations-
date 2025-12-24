from app.core.database import SessionLocal, engine, Base
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from datetime import datetime
import random

# Ensure tables exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ---------- CREATE CUSTOMERS ----------
customers = []
for i in range(1, 11):
    customer = Customer(
        name=f"Customer {i}",
        email=f"customer{i}@test.com",
    )
    db.add(customer)
    customers.append(customer)

db.commit()

# ---------- CREATE PRODUCTS ----------
products = []
categories = ["Electronics", "Accessories", "Home", "Fitness"]

for i in range(1, 21):
    product = Product(
        name=f"Product {i}",
        category=random.choice(categories),
        price=random.randint(500, 5000),
    )
    db.add(product)
    products.append(product)

db.commit()

# ---------- CREATE ORDERS ----------
for customer in customers:
    num_orders = random.randint(2, 5)

    for _ in range(num_orders):
        product = random.choice(products)

        order = Order(
            customer_id=customer.id,
            product_id=product.id,
            quantity=random.randint(1, 3),
            price=product.price,
            purchased_at=datetime.utcnow(),
        )
        db.add(order)

db.commit()
db.close()

print("✅ Seeded 10 customers, 20 products, and orders successfully!")
