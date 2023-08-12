# gui.py
import tkinter as tk
from menus import MainMenu

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart App")
        self.geometry("500x425")  # Adjust the window size
        self.menu = MainMenu(self)

def run_gui():
    app = Application()
    app.mainloop()
