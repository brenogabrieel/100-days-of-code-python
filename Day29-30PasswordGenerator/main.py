from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Password Generator
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# Save Password
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# Find Password
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0, pady=(0, 20))

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=5)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=5)

# Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "your-email@example.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3, sticky="EW", padx=(5, 0))

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW", pady=10)

button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="EW", padx=(5, 0))

window.mainloop()
