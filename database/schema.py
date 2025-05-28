from pydantic import BaseModel, Field
from typing import List, Optional

class MenuItemSchema(BaseModel):
    name: str
    category: str
    ingredients: List[str]
    region: str
    spiciness: str
    price: float
    ratings: float

class UserSearchSchema(BaseModel):
    region: str
    craving: str

class RecommendationSchema(BaseModel):
    user_id: str
    region: str
    craving: str
    menu_items: List[str]

class TrendDataSchema(BaseModel):
    food_item: str
    region: str
    trend_score: float
