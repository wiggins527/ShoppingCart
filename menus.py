# menus.py
import tkinter as tk
from tkinter import messagebox
from cart import Cart
from items import items_data

class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.cart = Cart()
        self.cart_menu_instance = None  # Store the CartMenu instance
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.shop_button = tk.Button(self, text="Shop", command=self.show_cart_menu)
        self.shop_button.pack()
        self.exit_button = tk.Button(self, text="Exit", command=self.parent.quit)
        self.exit_button.pack()

        self.cart_label = tk.Label(self, text="Total: $0.00")
        self.cart_label.pack()

    def show_cart_menu(self):
        if self.cart_menu_instance:  # Check if instance exists
            self.cart_menu_instance.destroy()  # Destroy the existing instance
        self.cart_menu_instance = CartMenu(self, self.cart, self.update_cart)  # Pass the update_cart method
        self.cart_menu_instance.pack()

    def update_cart(self):
        self.cart_label.config(text=f"Total: ${self.cart.calculate_total():.2f}")

class CartMenu(tk.Frame):
    def __init__(self, parent, cart, update_cart_callback):
        super().__init__(parent)
        self.parent = parent
        self.cart = cart
        self.update_cart_callback = update_cart_callback
        self.item_counters = {}  # Initialize the item_counters dictionary
        self.create_widgets()

    def create_widgets(self):
        for item_num, item_info in items_data.items():
            item_label = tk.Label(self, text=f"{item_info.name} - ${item_info.price:.2f}")
            item_label.pack()

            add_button = tk.Button(self, text="Add to Cart", command=lambda n=item_num: self.add_to_cart(n))
            add_button.pack()

            # Counter label for each item
            counter_label = tk.Label(self, text="Quantity: 0")
            counter_label.pack()
            self.item_counters[item_num] = counter_label

            remove_button = tk.Button(self, text="Remove from Cart", command=lambda n=item_num: self.remove_from_cart(n))
            remove_button.pack()

        checkout_button = tk.Button(self, text="Checkout", command=self.checkout)
        checkout_button.pack()

        reset_button = tk.Button(self, text="Reset Cart", command=self.reset_cart)
        reset_button.pack()

    def add_to_cart(self, item_num):
        self.cart.add_item(item_num)
        self.update_cart_callback()  # Update cart label in MainMenu
        self.update_item_counters()

    def remove_from_cart(self, item_num):
        if item_num in self.cart.items:
            if self.cart.items[item_num].quantity > 1:
                self.cart.items[item_num].quantity -= 1
            else:
                del self.cart.items[item_num]
        self.update_cart_callback()  # Update cart label in MainMenu
        self.update_item_counters()

    def update_item_counters(self):
        for item_num, counter_label in self.item_counters.items():
            cart_item = self.cart.items.get(item_num)
            quantity = cart_item.quantity if cart_item else 0
            counter_label.config(text=f"Quantity: {quantity}")

    def checkout(self):
        summary = "Checkout Summary:\n"
        for item_num, cart_item in self.cart.items.items():
            summary += f"{cart_item.item.name} - Quantity: {cart_item.quantity}\n"
        total = self.cart.calculate_total()
        summary += f"Total: ${total:.2f}"
        messagebox.showinfo("Checkout", summary)

    def reset_cart(self):
        self.cart.items.clear()
        self.update_cart_callback()  # Update cart label in MainMenu
        self.update_item_counters()
