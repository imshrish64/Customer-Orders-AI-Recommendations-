from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.repositories.order_repo import get_orders_for_customer
from app.repositories.product_repo import get_products
from app.services.recommendation_service import generate_recommendations
from app.schemas.recommendation import RecommendationResponse

router = APIRouter()


@router.post(
    "/customers/{customer_id}/recommendations",
    response_model=RecommendationResponse,
)
async def recommend_products(customer_id: int, db: Session = Depends(get_db)):
    # 1️⃣ Get last 5 orders
    orders = get_orders_for_customer(db, customer_id, limit=5)

    if not orders:
        raise HTTPException(
            status_code=404,
            detail="No purchase history available for recommendations",
        )

    # 2️⃣ Build product context
    product_map = {
        p.id: {"name": p.name, "category": p.category}
        for p in get_products(db)
    }

    purchased_products = [
        product_map[o.product_id]
        for o in orders
        if o.product_id in product_map
    ]

    # 3️⃣ Call async recommendation service
    recommendations = await generate_recommendations(purchased_products)

    return {
        "customer_id": customer_id,
        "recommendations": recommendations,
    }
