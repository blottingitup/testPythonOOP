from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("MyItem", 750)

# What if we want to restrict extra changes like item1.name = "OtherItem"
# Read-only attributes, encapsulation

# print(item1.read_only_name)
# item1.read_only_name = "BBB" :  error

# item1._name = "OtherItem": can still access to _name at instance level
# item1.__name: no access at all, acts like private

item1.name = "OtherItem"  # Calls "name" method (setter)
print(item1.name)  # Calls "name" method (getter)

item1.apply_increment(0.2)  # Encapsulation, no direct access to price
item1.apply_discount()
print(item1.price)  # Price is read-only, but can be changed via method

# item1.send_email(): not simple, but the whole complex operation is hidden

item2 = Phone("jscPhone", 1000, 3)
item2.apply_increment(0.2)  # Phone inherits from Item
print(item2.price)  # Thus using methods from parent class ("Item")

# Polymorphism in action:
# Built-in function "len" knows how to handle different types of objects

item3 = Keyboard("jscKeyboard", 1000, 3)
item3.apply_discount()  # "apply_discount" for "Keyboard"
print(item3.price)
