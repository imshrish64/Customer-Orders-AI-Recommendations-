from sqlalchemy.orm import Session
from app.models.product import Product


def create_product(db: Session, data: Product):
    product = Product(
        name=data.name,
        category=data.category,
        price=data.price,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session):
    return db.query(Product).all()
