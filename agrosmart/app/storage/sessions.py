from typing import Dict, Any
import json

class SessionStorage:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}
    
    def get_session(self, phone: str) -> Dict[str, Any]:
        return self.sessions.get(phone, {})
    
    def set_session(self, phone: str, data: Dict[str, Any]):
        self.sessions[phone] = data
    
    def update_session(self, phone: str, key: str, value: Any):
        if phone not in self.sessions:
            self.sessions[phone] = {}
        self.sessions[phone][key] = value