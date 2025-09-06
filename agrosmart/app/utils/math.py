def calculate_dose_per_hectare(product_dose: float, area: float) -> float:
    """Calcular dosis total según área"""
    return product_dose * area

def calculate_total_cost(products: list, quantities: list, prices: list) -> float:
    """Calcular costo total de productos"""
    return sum(q * p for q, p in zip(quantities, prices))

def calculate_application_rate(concentration: float, target_rate: float) -> float:
    """Calcular tasa de aplicación"""
    return target_rate / concentration if concentration > 0 else 0