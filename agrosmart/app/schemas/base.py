from pydantic import BaseModel
from datetime import datetime

class BaseSchema(BaseModel):
    created_at: datetime = None
    updated_at: datetime = None