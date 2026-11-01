import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

today = datetime.now()
username = os.getenv("PIXELA_USERNAME")
token = os.getenv("PIXELA_TOKEN")
ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
TODAY = today.strftime("%Y%m%d")

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-token": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{ID}"

pixel_config = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{ID}/{TODAY}"

pixel_update_config = {
    "quantity": "15"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)



pixel_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{ID}/{TODAY}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)