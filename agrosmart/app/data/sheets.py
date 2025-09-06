import gspread
from app.config import settings

class SheetsClient:
    def __init__(self):
        gc = gspread.service_account(filename=settings.google_sheets_credentials)
        self.sheet = gc.open_by_key(settings.google_sheets_id)
    
    def get_products(self):
        return self.sheet.worksheet("Productos").get_all_records()
    
    def update_products(self, df):
        worksheet = self.sheet.worksheet("Productos")
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())