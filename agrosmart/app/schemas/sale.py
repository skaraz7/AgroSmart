from pydantic import BaseModel
from typing import List
from .base import BaseSchema

class SaleItem(BaseModel):
    product_name: str
    quantity: int
    unit_price: int
    total: int

class Sale(BaseSchema):
    customer_phone: str
    items: List[SaleItem]
    total_amount: int
    status: str = "pending"