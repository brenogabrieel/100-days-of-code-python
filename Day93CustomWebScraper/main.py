import requests
from bs4 import BeautifulSoup
import csv

URL = "https://m.imdb.com/chart/moviemeter/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")

    all_movies = soup.find_all(name="h3", class_="ipc-title__text")
    movie_titles = [movie.getText() for movie in all_movies]

    # Write movie titles with ranking to CSV file
    with open("popularmoviesrn.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Ranking", "Movie Title"])
        for i, movie in enumerate(movie_titles, start=0):
            writer.writerow([i, movie])
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
