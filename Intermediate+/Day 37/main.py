import requests
from datetime import datetime

# GET
USERNAME = "jishooktt"
TOKEN = "2d3f8e0d50c024ccc"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# POST
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_creation_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours do you code today? "),
}

# response = requests.post(url=pixel_endpoint, json=pixel_creation_data, headers=headers)
# print(response.text)

# PUT
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "1",
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
