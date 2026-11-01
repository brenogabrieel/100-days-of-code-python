import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text




soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
# print(soup.prettify())
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    file.writelines([f"{movie}\n" for movie in movies])