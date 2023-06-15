#91906 2nd attempt

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("365x300")
        self.root.resizable(1, 1)

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
            col += 1
            if col > 3:
                col = 0
                row += 1



root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

