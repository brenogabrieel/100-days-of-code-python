from tkinter import *
import tkinter as tk

class DisappearingText(Tk):
    def __init__(self):
        super().__init__()
        self.title("DisappearingText")
        self.config(bg="#404040")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        self.title_label = Label()
        self.title_label.config(text="DisappearingText", font=("Arial", 50, "bold"), fg="#fafafa", bg="#000000", pady=20)
        self.title_label.grid(column=3, row=0, columnspan=3)

        self.explanation = Label()
        self.explanation.config(text="If you stop writing for more than 5 seconds, all your progress will be lost.", font=("Arial", 10), fg="#fafafa", bg="#000000", pady=20)
        self.explanation.grid(column=3, row=1, columnspan=3)




class UserWriting(Text):
    def __init__(self):
        super().__init__()
        self.config(width=51, height=5, font=("Helvetica", 20), bg="White", pady=20)
        self.grid(column=3, row=2, columnspan=3)

    def end_app(self):
        self.delete("1.0", END)


class StartButton(Button):
    def __init__(self):
        super().__init__()
        self.config(text="START", font=("Arial", 25, "bold"), bg="#000000", fg="#fafafa")
        self.grid(column=1, row=3)


class Timer(Label):
    def __init__(self):
        super().__init__()
        self.config(text="5 secs", font=("Arial", 30, "bold"), bg="#000000", fg="#fafafa")
        self.grid(column=7, row=3)
