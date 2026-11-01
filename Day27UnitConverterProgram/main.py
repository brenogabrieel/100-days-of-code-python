from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = round(1.609 * miles)
    answer.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="Is equal to", font=("Arial", 24))
my_label.grid(column=0, row=1)

answer = Label(text="0", font=("Arial", 24))
answer.grid(column=1, row=1)


miles_label = Label(text=" Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

km_label = Label(text="KM", font=("Arial", 24))
km_label.grid(column=2, row=1)

button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

window.mainloop()
