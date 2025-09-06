from typing import List
from app.schemas.product import Product

class RecommendationService:
    def __init__(self, repository):
        self.repository = repository
    
    def recommend_for_pest(self, pest: str, crop: str = None) -> List[Product]:
        """Recomendar productos para una plaga específica"""
        products = self.repository.search_products(pest)
        return sorted(products, key=lambda p: p.priority)
    
    def calculate_cost(self, products: List[Product], area: float) -> dict:
        """Calcular costo total para un área específica"""
        total = sum(p.sale_price for p in products)
        return {"total": total, "per_hectare": total / area if area > 0 else 0}