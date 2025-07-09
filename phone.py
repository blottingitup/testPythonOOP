from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        # super: can fully access the parent class
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to 0"

        # Assign to self object
        self.broken_phones = broken_phones
