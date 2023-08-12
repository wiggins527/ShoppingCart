# models.py
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
