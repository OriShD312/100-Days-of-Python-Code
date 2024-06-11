import os
import requests
from datetime import datetime

# PARAMETERS #
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "orish92"
GRAPH = "mygraph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# GRAPH CREATION #
# pixela_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)

# GRAPH CONFIGURATION #
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH,
#     "name": "My First Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "sora"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# FIRST GRAPH UPDATE #
today = datetime.today().strftime("%Y%m%d")
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}"
graph_update = {
    "date": today,
    "quantity": input("How many hours did I practice today? ")
}

response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# UPDATING A SPECIFIC DATE ON THE GRAPH #
# pixel_update = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/{today}"
# pixel_params = {
#     "quantity": "6"
# }

# response = requests.put(url=pixel_update, json=pixel_params, headers=headers)
# print(response.text)

# DELETING AN ENTRY FROM THE GRAPH #
# pixel_delete = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}/{today}"
# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)
