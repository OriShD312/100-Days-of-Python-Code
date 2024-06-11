import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}

GOOGLE_SHEETS_URL = os.environ.get("GOOGLE_URL")

# Get exercise data from user
nutritionix_params = {
    "query": input("What was your exercise? ")
}

response = requests.post(url=NUTRITIONIX_URL, json=nutritionix_params, headers=NUTRITIONIX_HEADERS)

# POST exercise data to Google Sheet with 3 different authentication methods tested
# Using Bearer token
sheets_headers = {
    "Authorization": os.environ.get("TOKEN")
}

# Using Basic generated token
# sheets_headers = {
#     "Authorization": "Basic dGVzdDp0ZXN0"
# }

# Using HTTP Basic authentication method with username and password
# basic = HTTPBasicAuth("test", "test")

now = datetime.now()
for exercise in response.json()["exercises"]:
    body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M"),
            "exercise": exercise["name"].title(),
            "duration [min]": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(url=GOOGLE_SHEETS_URL, json=body, headers=sheets_headers)

print("Done")
