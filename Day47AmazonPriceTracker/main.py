import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
YOUR_SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
YOUR_EMAIL = os.getenv("EMAIL_ADDRESS")
YOUR_PASSWORD = os.getenv("EMAIL_PASSWORD")

URL = "https://www.amazon.com.br/Silmarillion-J-R-Tolkien/dp/0007264895"
header = {'Accept-Language': "pt-BR,pt;q=0.9",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0"}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1].strip()
# Brazilian format: 1.234,56 -> 1234.56
price_as_float = float(price_without_currency.replace(".", "").replace(",", "."))
print("$"+price_without_currency)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 650

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )