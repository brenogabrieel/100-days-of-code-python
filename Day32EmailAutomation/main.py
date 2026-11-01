import random
import smtplib
import datetime as dt
import pandas
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    person_data = birthdays_dict[today]
    name = person_data["name"]
    email = person_data["email"]

    letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    random_letter = random.choice(letter_templates)

    with open(random_letter) as file:
        letter_content = file.read()
        letter_content = letter_content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday\n\n{letter_content}")
