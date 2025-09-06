from fastapi import APIRouter, Request, Depends
from app.whatsapp.client import WhatsAppClient
from app.deps import get_whatsapp_client

router = APIRouter()

@router.get("/")
def verify_webhook(hub_mode: str, hub_verify_token: str, hub_challenge: str):
    if hub_mode == "subscribe" and hub_verify_token == "verify_token":
        return int(hub_challenge)
    return {"error": "Invalid verification"}

@router.post("/")
def receive_message(request: Request, wa_client: WhatsAppClient = Depends(get_whatsapp_client)):
    # Procesar mensaje entrante
    return {"status": "received"}