#91906 2nd attempt

import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkmacosx import Button

DEFAULT_FONT_STYLE = ("Arial", 24)
LARGE_FONT = ("Arial", 40, "bold")
SMALL_FONT = ("Arial", 16)
DIGITS_FONT = ("Arial", 24, "bold")

WHITE = "#FFFFFF"
CREAM = "#F8FAFF"
LABEL_COLOUR = "#25265E"
LIGHT_GRAY = "#F5F5F5"
LIGHT_BLUE = "#CCEDFF"
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x600")
        self.root.resizable(0, 0)
        self.root.configure(background="white")

        self.sum_expression = "0"
        self.current_expression = "0"
        self.display_frame=self.create_display_frame()
        self.sum_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "\u2212", "+": "+"}

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_buttons()

    def create_buttons(self):
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()

    def create_display_frame(self):
        frame=tk.Frame(self.root, bg=LIGHT_GRAY)
        frame.grid(columnspan=4, sticky="nsew")
        return(frame)

    def create_buttons_frame(self):
        frame=tk.Frame(self.root, bg="green")
        frame.grid(sticky="nsew")
        return(frame)

    def create_display_labels(self):
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)
        sum_label = tk.Label(self.display_frame, text=self.sum_expression, anchor=tk.E,
                             bg=LIGHT_GRAY, fg=LABEL_COLOUR,padx=24, font=SMALL_FONT)
        sum_label.grid(sticky="e")

        label = tk.Label(self.display_frame, text=self.current_expression,
                             bg=LIGHT_GRAY, fg=LABEL_COLOUR,padx=24, font=LARGE_FONT)
        label.grid(sticky="e")

        return(sum_label,label)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, highlightbackground=CREAM,
                               fg=LABEL_COLOUR, font=DIGITS_FONT,borderwidth=1)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), highlightbackground=WHITE,
                               fg=LABEL_COLOUR, font=DIGITS_FONT,borderwidth=1)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", highlightbackground=WHITE,
                           fg=LABEL_COLOUR, font=DIGITS_FONT,borderwidth=1)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", highlightbackground=LIGHT_BLUE,
                           fg=LABEL_COLOUR, font=DIGITS_FONT,borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

root = tk.Tk()
root.attributes('-alpha',0.95)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
calculator = Calculator(root)
root.mainloop()

