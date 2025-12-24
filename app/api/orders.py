from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.repositories.order_repo import create_order, get_orders_for_customer

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create_order_api(
    payload: OrderCreate,
    db: Session = Depends(get_db),
):
    """
    Create a purchase/order
    """
    return create_order(db, payload)


@router.get(
    "/customer/{customer_id}",
    response_model=list[OrderResponse],
)
def list_orders_for_customer(
    customer_id: int,
    db: Session = Depends(get_db),
):
    orders = get_orders_for_customer(db, customer_id)

    if not orders:
        raise HTTPException(
            status_code=404,
            detail="No orders found for this customer",
        )

    return orders
