from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def flip_cards():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(back_card, image=card_back)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_cards()
def next_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(back_card, image=card_front)
    flip_timer = window.after(3000, func=flip_cards)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_cards)


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
canvas.create_image(400, 263, image=card_front)
back_card = canvas.create_image(400, 263, image=card_back)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)



button_known = Button(image=right, highlightthickness=0, command=is_known)
button_known.grid(column=1, row=1)

button_unknown = Button(image=wrong, highlightthickness=0, command=next_cards)
button_unknown.grid(column=0, row=1)

next_cards()

window.mainloop()
