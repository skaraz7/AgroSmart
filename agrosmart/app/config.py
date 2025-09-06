from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    whatsapp_token: str
    whatsapp_verify_token: str
    openai_api_key: str
    google_sheets_credentials: str
    google_sheets_id: str
    
    class Config:
        env_file = ".env"

settings = Settings()