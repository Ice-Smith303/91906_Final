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
        self.entry_field = tk.Entry(self.root, font=("Roboto", 20), justify="center")
        self.entry_field.grid(row=0, column=0, sticky="n")

        # Buttons
        column1x = 40
        column2x = 105
        column3x = 170
        column4x = 235

        row1y = 100
        row2y = 160
        row3y = 220
        row4y = 280

        # num column 1
        number7 = tk.Button(root, text='7', font='broadway 32', bg='yellow',
                         height=1, width=1)
        canvas.create_window(column1x, row1y, window=number7)

        number4 = tk.Button(root, text='4', font='broadway 32', bg='yellow',
                         height=1, width=1)
        canvas.create_window(column1x, row2y, window=number4)

        number1 = tk.Button(root, text='1', font='broadway 32', bg='yellow',
                         height=1, width=1)
        canvas.create_window(column1x, row3y, window=number1)


root = tk.Tk()
canvas = tk.Canvas(root, width=273, height=400, bg='lightblue')
canvas.grid()
calculator = Calculator(root)
root.mainloop()

