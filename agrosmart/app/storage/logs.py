import logging
from datetime import datetime

class ConversationLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("agrosmart")
    
    def log_message(self, phone: str, message: str, direction: str):
        """Registrar mensaje entrante o saliente"""
        self.logger.info(f"{direction} | {phone} | {datetime.now()} | {message}")
    
    def log_recommendation(self, phone: str, query: str, products: list):
        """Registrar recomendación realizada"""
        self.logger.info(f"RECOMMENDATION | {phone} | {query} | {len(products)} products")