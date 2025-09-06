from app.schemas.sale import Sale, SaleItem
from typing import List

class OrderService:
    def create_order(self, customer_phone: str, products: List[dict]) -> Sale:
        """Crear una nueva orden de venta"""
        items = []
        total = 0
        
        for product in products:
            item = SaleItem(
                product_name=product["name"],
                quantity=product["quantity"],
                unit_price=product["price"],
                total=product["quantity"] * product["price"]
            )
            items.append(item)
            total += item.total
        
        return Sale(
            customer_phone=customer_phone,
            items=items,
            total_amount=total
        )