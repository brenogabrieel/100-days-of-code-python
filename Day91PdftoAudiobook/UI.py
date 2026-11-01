from tkinter import *


class Pdftomp3(Tk):
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

