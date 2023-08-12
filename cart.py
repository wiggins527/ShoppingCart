# cart.py
from models import CartItem
from items import items_data

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_num):
        if item_num in items_data:
            if item_num in self.items:
                self.items[item_num].quantity += 1
            else:
                self.items[item_num] = CartItem(items_data[item_num], 1)

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item.item.price * item.quantity
        return total
