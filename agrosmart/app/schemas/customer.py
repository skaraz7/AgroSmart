from pydantic import BaseModel
from .base import BaseSchema

class Customer(BaseSchema):
    phone: str
    name: str
    location: str = None
    farm_size: float = None