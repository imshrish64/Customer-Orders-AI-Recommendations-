from sqlalchemy.orm import Session
from app.models.customer import Customer

def create_customer(db: Session, name: str, email: str) -> Customer:
    customer = Customer(name=name, email=email)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customers(db: Session):
    return db.query(Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()
