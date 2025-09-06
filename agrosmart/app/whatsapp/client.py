import requests
from app.config import settings

class WhatsAppClient:
    def __init__(self):
        self.token = settings.whatsapp_token
        self.base_url = "https://graph.facebook.com/v17.0"
    
    def send_message(self, to: str, message: str):
        url = f"{self.base_url}/messages"
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "text": {"body": message}
        }
        return requests.post(url, headers=headers, json=data)