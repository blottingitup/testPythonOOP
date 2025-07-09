import csv

class Item:
    pay_rate = 0.8 # Class attribute
    all = []

    # Magic method __init__ is initialized when instance is created
    def __init__(self, name: str, price: float, quantity=0):  # Initialize arguments, differentiate mandatory parameters
        # assert: Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to 0"

        # Assign to self object
        self.__name = name  # __: Read-only
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name  # __: Read-only

    @name.setter  # Set value of name even if name is read-only attribute
    def name(self, value):
        if len(value) > 10:  # Can add conditions
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # Use CSV for storing data, items.csv
    # Class method: can be accessed from class level only
    # cls: class object is passed as first argument
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    # Static method: no need to send object as first argument
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Difference from __str__:
    def __repr__(self):  # Represent
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"
    '''
    @property
    def read_only_name(self):
        return "AAA"
    '''
