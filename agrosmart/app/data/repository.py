from typing import List, Optional
from app.schemas.product import Product
from app.schemas.customer import Customer
from app.data.sheets import SheetsClient

class Repository:
    def __init__(self, sheets: SheetsClient):
        self.sheets = sheets
    
    def get_products(self) -> List[Product]:
        data = self.sheets.get_products()
        return [Product(**row) for row in data]
    
    def search_products(self, query: str) -> List[Product]:
        products = self.get_products()
        return [p for p in products if query.lower() in p.name.lower()]