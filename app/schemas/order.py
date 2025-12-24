from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrderCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    price: float

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    price: float
    purchased_at: datetime

    model_config = ConfigDict(from_attributes=True)
