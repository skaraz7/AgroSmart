from fastapi import FastAPI
from app.whatsapp.webhook import router as whatsapp_router

app = FastAPI(title="AgroSmart", version="0.1.0")

app.include_router(whatsapp_router, prefix="/webhook")

@app.get("/")
def root():
    return {"message": "AgroSmart API"}