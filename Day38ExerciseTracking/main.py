import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("SHEETY_ENDPOINT")

QUERY_QUESTION = input("Tell me which exercises you did: ")

GENDER = "MALE"
WEIGHT_KG = "75"
HEIGHT_CM = "175"
AGE = "25"


user_params = {
    "query": QUERY_QUESTION,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)