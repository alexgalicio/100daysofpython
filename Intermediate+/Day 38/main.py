import requests
from datetime import datetime

PROMPT = input("Tell me which exercises you did: ")
GENDER = "female"
WEIGHT_KG = 45
HEIGHT_CM = 150
AGE = 18

API_KEY = "163443e85f8d521a7645907f616d98af	"
APP_ID = "4c6231a4"
USERNAME = "87af551781466f4c3fbb7152bc76f443"
TOKEN = "amlzdWxmdXI6enh6Y3p4emM"

sheety_endpoint = "https://api.sheety.co/87af551781466f4c3fbb7152bc76f443/workoutTracking/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": PROMPT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
results = response.json()
# print(results)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

basic_auth = {
    "Authorization": f"Basic {TOKEN}"
}

for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=basic_auth)
    print(sheet_response.text)
