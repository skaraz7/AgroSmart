import pandas as pd
from app.data.sheets import SheetsClient

def seed_products():
    """Importar Excel de productos a Google Sheets"""
    df = pd.read_excel("productos_unificado.xlsx")
    sheets = SheetsClient()
    sheets.update_products(df)
    print(f"Importados {len(df)} productos a Google Sheets")

if __name__ == "__main__":
    seed_products()