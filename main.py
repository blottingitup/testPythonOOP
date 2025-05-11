class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    # Magic method __init__ is initialized when instance is created
    def __init__(self, name: str, price: float, quantity=0): # Initialize arguments, differentiate mandatory parameters
        # assert: Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.__dict__) # __dict__ shows all the attributes
print(item1.__dict__)
