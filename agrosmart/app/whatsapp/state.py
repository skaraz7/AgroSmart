from enum import Enum

class ConversationState(Enum):
    INITIAL = "initial"
    WAITING_QUERY = "waiting_query"
    WAITING_AREA = "waiting_area"
    SHOWING_PRODUCTS = "showing_products"
    CREATING_ORDER = "creating_order"

class StateManager:
    def __init__(self):
        self.states = {}
    
    def get_state(self, phone: str) -> ConversationState:
        return self.states.get(phone, ConversationState.INITIAL)
    
    def set_state(self, phone: str, state: ConversationState):
        self.states[phone] = state