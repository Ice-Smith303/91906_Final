#91906 2nd attempt

import customtkinter as ctk
import tkinter as tk
from tkinter import *


LIGHT_GRAY = "#F5F5F5"
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(1, 1)
        self.root.configure(background="white")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_frame(self):
        frame=tk.Frame(self.root, height=221, bg="blue")
        frame.grid(columnspan=2, sticky="nsew")


    def create_buttons_frame(self):
        frame=tk.Frame(self.root)
        frame.grid(sticky="nsew", columnspan=2)





        # Entry Field
        self.entry_field = tk.Entry(self.root, font=("Helvetica", 20), justify="right")
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button in buttons:
            btn = tk.Button(self.root, text=button, width=5, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.bind("<Button-1>")
            root.grid_columnconfigure(col, weight=1)
            root.grid_rowconfigure(row, weight=1)
            col += 1
            if col > 3:
                col = 0
                row += 1





root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

