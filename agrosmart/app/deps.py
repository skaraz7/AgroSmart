from functools import lru_cache
from app.data.sheets import SheetsClient
from app.whatsapp.client import WhatsAppClient
from app.ai.orchestrator import AIOrchestrator

@lru_cache()
def get_sheets_client():
    return SheetsClient()

@lru_cache()
def get_whatsapp_client():
    return WhatsAppClient()

@lru_cache()
def get_ai_orchestrator():
    return AIOrchestrator()