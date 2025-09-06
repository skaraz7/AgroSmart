from pydantic import BaseModel
from .base import BaseSchema

class Product(BaseSchema):
    name: str
    category: str
    active_ingredient: str
    days_to_harvest: int
    priority: str
    purchase_price: int
    sale_price: int