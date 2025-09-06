from pydantic import BaseModel

class WhatsAppMessage(BaseModel):
    from_number: str
    message_body: str
    message_id: str

class WhatsAppWebhook(BaseModel):
    object: str
    entry: list