import requests
from random import randint
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://the-one-api.dev/v2/"
headers = {'Authorization': f"Bearer {os.getenv('ONE_API_TOKEN')}"}

app = Flask(__name__, static_url_path='/static')

quote_data = requests.get(url=f"{URL}/quote", headers=headers)
quote_data.raise_for_status()
data = quote_data.json()

def get_character_image_url(character):
    fandom_url = f"https://lotr.fandom.com/wiki/{character.replace(' ', '_')}"
    response = requests.get(fandom_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_url = None
    infobox = soup.find('aside', class_='portable-infobox')
    if infobox:
        image_element = infobox.find('img')
        if image_element:
            image_url = image_element['src']
    print("Image URL:", image_url)  # Add this line for debugging
    return image_url




def generate_quote():
    random_number = randint(0, 999)
    quote_json = data["docs"][random_number]
    quote = quote_json["dialog"]
    character_id = quote_json["character"]
    character_data = requests.get(url=f"{URL}character/{character_id}", headers=headers)
    character_data.raise_for_status()
    character_json = character_data.json()
    character = character_json['docs'][0]["name"]
    movie_id = quote_json["movie"]
    movie_data = requests.get(url=f"{URL}movie/{movie_id}", headers=headers)
    movie_data.raise_for_status()
    movie_json = movie_data.json()
    movie = movie_json['docs'][0]['name']
    wiki_link = character_json['docs'][0]["wikiUrl"]
    character_image_url = get_character_image_url(character)
    print("Character Image URL:", character_image_url)

    return quote, character, wiki_link, movie, character_image_url

initial_quote, initial_character, initial_wiki_link, initial_movie, initial_character_image_url = generate_quote()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('generate_quote') == 'true':
        quote, character, wiki_link, movie, character_image_url = generate_quote()
        print("Character Image URL:", character_image_url)  # Debugging
        return render_template('index.html', quote=quote, character=character, movie=movie, link=wiki_link, character_image_url=character_image_url)
    return render_template('index.html', quote=initial_quote, character=initial_character, movie=initial_movie, link=initial_wiki_link, character_image_url=initial_character_image_url)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
