# 91906 Calculator Ice Smith 2023

import random
import tkinter as tk

# Defining Constants that define font, size and weight.
DEFAULT_FONT_STYLE = ("Arial", 24)
LARGE_FONT = ("Arial", 40, "bold")
SMALL_FONT = ("Arial", 16)
DIGITS_FONT = ("Arial", 24, "bold")

WHITE = "#FFFFFF"
CREAM = "#F8FAFF"
LABEL_COLOUR = "#25265E"
LIGHT_GRAY = "#F5F5F5"
LIGHT_BLUE = "#CCEDFF"

QUESTION_1 = "Solve the equation"


class HomePage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.quiz_window = None
        self.root = None
        self.main_window.title("Home Page")
        self.main_window.configure(background="white")
        self.main_window.minsize(300, 350)

        main_window.columnconfigure(0, weight=1)
        main_window.rowconfigure(0, weight=1)

        self.top_frame = tk.Frame(main_window, bg="cornflowerblue")
        self.top_frame.grid(column=0, row=0, sticky="nsew")
        self.button_frame = tk.Frame(main_window)
        self.button_frame.grid(column=0, row=1, sticky="nsew")

        self.button_frame.columnconfigure(0, weight=1)
        for i in range(3):
            self.button_frame.rowconfigure(i, weight=1)

        self.create_calculator_button()
        self.create_quiz_button()
        self.create_quit_button()

        self.main_window.columnconfigure(0, weight=1)

        self.create_text()

    def create_text(self):
        title = tk.Label(self.top_frame, text="Leap Frog Education", font=LARGE_FONT, bg="cornflowerblue", fg="white")
        title.grid(padx=10)

    def call_calculator(self):
        # if self.root.state() == "disabled":
        # if self.root.winfo_exists:
        try:
            if self.root != None:
                self.root.destroy()
            self.root = tk.Tk()  # creating window
            self.calculator = Calculator(self.root)  # creating object of class by passing window.
            self.root.mainloop()
        except:
            self.root = tk.Tk()  # creating window
            self.calculator = Calculator(self.root)  # creating object of class by passing window.
            self.root.mainloop()

    def create_quit_button(self):
        button = tk.Button(self.button_frame, text="Quit Windows", command=lambda: self.quit_windows())
        button.grid(sticky="ew")

    def quit_windows(self):
        self.main_window.destroy()
        try:
            self.quiz_window.destroy()
        except:
            pass
        try:
            self.root.destroy()
        except:
            pass

    def create_calculator_button(self):
        button = tk.Button(self.button_frame, text="Calculator", command=lambda: self.call_calculator())
        button.grid(sticky="ew")

    def create_quiz_button(self):
        button = tk.Button(self.button_frame, text="Quiz page", command=lambda: self.create_quiz_window())
        button.grid(sticky="ew")

    def create_quiz_window(self):
        try:
            if self.quiz_window != None:
                self.quiz_window.destroy()
            self.quiz_window = tk.Tk()
            self.quizpage1 = QuizPage(self.quiz_window)
            self.quiz_window.mainloop()
        except:
            self.quiz_window = tk.Tk()
            self.quizpage1 = QuizPage(self.quiz_window)
            self.quiz_window.mainloop()


class QuizPage:
    def __init__(self, quiz_window):
        quiz_window.title("Quiz Page")
        quiz_window.configure(background="white")
        quiz_window.resizable(0, 0)

        top_label = tk.Label(quiz_window, text="Solve the Equations:\n", background="white", fg="black",
                             font=DEFAULT_FONT_STYLE)
        top_label.grid(row=0, sticky="nsew", padx=50, columnspan=2)

        self.entry_frame = tk.Frame(quiz_window, background="white", width = 100)
        self.entry_frame.grid(row=1, column=1, sticky="nsew")

        self.quest_frame = tk.Frame(quiz_window, background="white")
        self.quest_frame.grid(row = 1, column = 0, sticky="nsew")
        self.question_maker(self.quest_frame)
        self.entry_maker(self.entry_frame)


        quiz_window.columnconfigure(0, weight=1)
        quiz_window.columnconfigure(1, weight=1)
        quiz_window.rowconfigure(0, weight=1)
        quiz_window.rowconfigure(1, weight=1)





    def question_maker(self, quest_frame):
        for i in range(10):
            randnum1 = random.randint(11, 99)
            randnum2 = random.randint(11, 99)
            #final_quest = QUESTION_1 + " " + str(randnum1) + " + " + str(randnum2)
            question_label = tk.Label(quest_frame, text=(str(randnum1) + " + " + str(randnum2)), background="white", fg="black", font=DEFAULT_FONT_STYLE)
            question_label.grid(row=i, sticky="nsw", padx=10)
            quest_frame.rowconfigure(i, weight=1)
            quest_frame.columnconfigure(0, weight=1)

    def entry_maker(self, entry_frame):
        for i in range(10):
            entry_box = tk.Entry(entry_frame, background="white", fg="black")
            entry_box.grid(row=i, sticky="nsew", padx=10, pady=2)
            entry_frame.rowconfigure(i, weight=1)
            entry_frame.columnconfigure(0, weight=1)



class Calculator:
    def __init__(self, root):
        # initializing and defining window attributes
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(1, 1)
        self.root.configure(background="black")
        self.root.attributes('-alpha', 0.94)
        self.root.minsize(150, 350)

        # defining data structures
        self.current_expression = ""
        self.current_expression_base = ""
        self.sum_result = ""
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "\u2212", "+": "+"}

        # calling methods to create frames, labels and buttons
        self.create_frames_labels()
        self.create_buttons()

        # assigning weight to Window Frames so that they expand to window size.
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        # Assigning weight to buttons within the buttons_frame frame so that they expand to frame size.
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.is_first_press = True
        self.error = False
        self.percentage_val = 0

    # creates display_frame that will hold display labels.
    def create_display_frame(self):
        frame = tk.Frame(self.root, bg=LIGHT_GRAY)
        frame.grid(columnspan=4, sticky="nsew")
        return frame

    # Creates buttons_frame that will hold buttons.
    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg="green")
        frame.grid(sticky="nsew")
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)
        return frame

    # calling method that calls the class methods that create the calculator frames and labels.
    def create_frames_labels(self):
        self.display_frame = self.create_display_frame()
        self.sum_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

    # calling method that calls the class methods that create the calculator buttons.
    def create_buttons(self):
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_percent_button()
        self.create_equals_button()

    def add_to_label(self, value):
        if self.is_first_press:
            self.is_first_press = False
            self.current_expression_base += str(self.sum_result)
        if self.error:
            self.current_expression = ""
            self.current_expression_base = ""
            self.update_label()
            self.update_sum_label()
            self.error = False
        self.current_expression += str(value)  # adds digit to displayed expression as typing
        self.current_expression_base += str(value)  # adds digit to expression with non unicode operators for math
        self.update_label()  # calls update_label, changes label text to current_expression with fancy unicode

    def append_operator(self, symbol, operator):
        if self.is_first_press:
            self.is_first_press = False
            self.current_expression_base += str(self.sum_result)  # previous result added to start for math BIMDAS
        if self.error == False:
            self.current_expression += (
                    " " + symbol + " ")  # operator added to expression you see as you type (unicode)
            self.current_expression_base += (" " + operator + " ")  # operator added not unicode
            self.update_label()

    # Creates display labels that display the summation and the expression on seperate lines.
    def create_display_labels(self):
        sum_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                             bg=LIGHT_GRAY, fg=LABEL_COLOUR, padx=24, font=SMALL_FONT)
        sum_label.grid(sticky="e")

        label = tk.Label(self.display_frame, text=self.current_expression,
                         bg=LIGHT_GRAY, fg=LABEL_COLOUR, padx=24, font=LARGE_FONT)
        label.grid(sticky="e")
        return sum_label, label

    # creates operator buttons.
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, highlightbackground=CREAM,
                               fg=LABEL_COLOUR, font=DIGITS_FONT, borderwidth=1,
                               command=lambda i=symbol, j=operator: self.append_operator(i, j))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # creates digit buttons
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), highlightbackground=WHITE,
                               fg=LABEL_COLOUR, font=DIGITS_FONT, borderwidth=1,
                               command=lambda i=digit: self.add_to_label(i))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # creates clear button
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", highlightbackground=WHITE,
                           fg=LABEL_COLOUR, font=DIGITS_FONT, borderwidth=1, command=lambda: self.clear_button_true())
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW)

    # creates equals button
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", highlightbackground=LIGHT_BLUE,
                           fg=LABEL_COLOUR, font=DIGITS_FONT, borderwidth=0, command=lambda: self.equals_button_true())
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_percent_button(self):
        button = tk.Button(self.buttons_frame, text="\u0025", highlightbackground=CREAM,
                           fg=LABEL_COLOUR, font=DIGITS_FONT, borderwidth=1, command=lambda: self.percentage())
        button.grid(row=0, column=3, columnspan=1, sticky=tk.NSEW)

    def percentage(self):
        if not self.error:
            try:
                if self.sum_result == "":
                    self.is_first_press = True
                    self.percentage_val = eval(self.current_expression_base) / 100
                    self.current_expression = self.percentage_val
                    self.current_expression = str(self.current_expression)[:12]
                    self.current_expression_base = ''
                    self.update_label()
                    self.update_sum_label()
                    self.sum_result = str(self.current_expression)

                else:
                    self.is_first_press = True
                    self.sum_result = float(self.sum_result) / 100
                    self.current_expression = (format(self.sum_result, '.12f')).rstrip("0")
                        # formats the scientific notation to standard notation so that the calculator displays precise value
                    self.update_label()
                    self.update_sum_label()

            except:
                self.current_expression = ""
                self.update_sum_label()
                self.current_expression = "Syntax Error"
                self.update_label()
                self.error = True

    def equals_button_true(self):
        try:
            self.update_sum_label()
            self.sum_result = eval(self.current_expression_base)
            self.current_expression = str(eval(self.current_expression_base))
            self.current_expression = self.current_expression[:8]
            self.current_expression_base = ""
        except:
            self.current_expression = "Syntax Error"
            self.current_expression_base = ""
            self.update_sum_label()
            self.error = True
        finally:
            self.update_label()
            self.is_first_press = True

    def clear_button_true(self):
        self.current_expression = ""
        self.current_expression_base = ""
        self.sum_result = ""
        self.update_label()
        self.update_sum_label()

    def update_sum_label(self):
        self.sum_label.config(text=self.current_expression_base)

    def update_label(self):
        self.label.config(text=self.current_expression)


main_window = tk.Tk()
page = HomePage(main_window)
main_window.mainloop()
