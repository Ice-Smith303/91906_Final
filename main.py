#91906 2nd attempt

import customtkinter as ctk
import tkinter as tk
from tkinter import *

WHITE = "#FFFFFF"
LARGE_FONT = ("Arial", 40, "bold")
SMALL_FONT = ("Arial", 16)
DIGITS_FONT = ("Arial", 24, "bold")
LABEL_COLOUR = "#25265E"
LIGHT_GRAY = "#F5F5F5"
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(1, 1)
        self.root.configure(background="white")

        self.sum_expression = "0"
        self.current_expression = "0"
        self.display_frame=self.create_display_frame()

        self.sum_label, self.label = self.create_display_labels()

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_digit_buttons()


    def create_display_frame(self):
        frame=tk.Frame(self.root, height=221, bg="blue")
        frame.grid(columnspan=2, sticky="nsew")
        return(frame)

    def create_buttons_frame(self):
        frame=tk.Frame(self.root)
        frame.grid(sticky="nsew", columnspan=2)
        return(frame)

    def create_display_labels(self):
        sum_label = tk.Label(self.display_frame, text=self.sum_expression,
                             bg=LIGHT_GRAY, fg=LABEL_COLOUR,padx=24, font=SMALL_FONT)
        sum_label.grid(sticky="nsew")

        label = tk.Label(self.display_frame, text=self.current_expression,
                             bg=LIGHT_GRAY, fg=LABEL_COLOUR,padx=24, font=LARGE_FONT)
        label.grid(sticky="nsew")

        return(sum_label,label)




        # Entry Field
        self.entry_field = tk.Entry(self.root, font=("Helvetica", 20), justify="right")
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOUR, font=DIGITS_FONT,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)




root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

