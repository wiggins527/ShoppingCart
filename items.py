# items.py
import json
from models import Item

def load_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items_data = json.load(file)
            items = {int(item_num): Item(item_info["name"], item_info["price"]) for item_num, item_info in items_data.items()}
            return items
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_items_to_file(items, filename):
    items_data = {item_num: {"name": item.name, "price": item.price} for item_num, item in items.items()}
    with open(filename, "w") as file:
        json.dump(items_data, file, indent=4)

items_data_file = "items.json"
items_data = load_items_from_file(items_data_file)
