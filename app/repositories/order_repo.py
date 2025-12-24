from sqlalchemy.orm import Session
from app.models.order import Order

def create_order(db: Session, data):
    """
    Create a new order
    """
    order = Order(**data.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders_for_customer(
    db: Session,
    customer_id: int,
    limit: int = 5
):
    """
    Fetch recent orders for a customer (default: last 5)
    """
    return (
        db.query(Order)
        .filter(Order.customer_id == customer_id)
        .order_by(Order.purchased_at.desc())
        .limit(limit)
        .all()
    )
