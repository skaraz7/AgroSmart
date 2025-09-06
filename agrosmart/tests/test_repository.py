import pytest
from app.data.repository import Repository
from app.data.sheets import SheetsClient

def test_get_products():
    sheets = SheetsClient()
    repo = Repository(sheets)
    products = repo.get_products()
    assert isinstance(products, list)

def test_search_products():
    sheets = SheetsClient()
    repo = Repository(sheets)
    results = repo.search_products("test")
    assert isinstance(results, list)