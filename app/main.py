from fastapi import FastAPI
from app.api import customers, products, orders, recommendations
from app.core.database import engine, Base

# 👇 import models so SQLAlchemy knows about them
from app.models.customer import Customer
from app.models.order import Order
from app.models.product import Product

app = FastAPI(title="Customer Orders & AI Recommendations (POC)")


@app.on_event("startup")
def on_startup():
    """
    POC-only: create tables automatically
    """
    Base.metadata.create_all(bind=engine)


app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(recommendations.router, tags=["Recommendations"])


@app.get("/health")
async def health():
    return {"status": "ok"}
