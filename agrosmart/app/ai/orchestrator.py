from openai import OpenAI
from app.config import settings
from app.ai.tools import get_available_tools

class AIOrchestrator:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.tools = get_available_tools()
    
    def process_message(self, message: str, context: dict = None):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            tools=self.tools
        )
        return response.choices[0].message.content