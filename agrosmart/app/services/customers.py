from app.schemas.customer import Customer

class CustomerService:
    def __init__(self, repository):
        self.repository = repository
    
    def get_or_create_customer(self, phone: str, name: str = None) -> Customer:
        """Obtener cliente existente o crear uno nuevo"""
        # Buscar cliente existente
        customer = self.repository.get_customer_by_phone(phone)
        
        if not customer:
            customer = Customer(
                phone=phone,
                name=name or f"Cliente {phone[-4:]}"
            )
            self.repository.save_customer(customer)
        
        return customer