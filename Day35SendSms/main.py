import requests
import os
from dotenv import load_dotenv
#use email to send weather
load_dotenv()
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")

weather_params = {
    "lat": 51.759050,
    "lon": 19.458600,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"]

will_rain = False



for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    
    print("Bring an umbrella.")
# print(weather_data["hourly"][0]["weather"][0]["id"])