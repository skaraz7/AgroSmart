import pytest
from app.ai.tools import search_products, calculate_dose

def test_search_products():
    result = search_products("fungicida")
    assert isinstance(result, list)

def test_calculate_dose():
    result = calculate_dose("Producto Test", 2.5)
    assert result is not None