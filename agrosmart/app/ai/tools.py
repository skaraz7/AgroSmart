def search_products(query: str):
    """Buscar productos por nombre o ingrediente activo"""
    # Implementar búsqueda
    pass

def calculate_dose(product: str, area: float):
    """Calcular dosis recomendada para un área específica"""
    # Implementar cálculo
    pass

def get_available_tools():
    return [
        {
            "type": "function",
            "function": {
                "name": "search_products",
                "description": "Buscar productos agrícolas",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    }
                }
            }
        }
    ]