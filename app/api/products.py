from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.repositories.product_repo import create_product, get_products

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product_api(
    payload: ProductCreate,
    db: Session = Depends(get_db),
):
    """
    Create a product
    """
    return create_product(db, payload)


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    """
    List all products
    """
    return get_products(db)
