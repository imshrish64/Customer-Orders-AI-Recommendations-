from pydantic import BaseModel
from typing import List


class RecommendationItem(BaseModel):
    product_name: str
    category: str
    reason: str


class RecommendationOutput(BaseModel):
    recommendations: List[RecommendationItem]
