import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "nickg"
GRAPH_ID = "graph1"
user_params = {
    "token": "dfksjkdiejialidue2",
    "username": "nickg",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## Configuring graphs.

graph_endpoint = "https://pixe.la/v1/users/nickg/graphs"
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers ={
"X-USER-TOKEN": "dfksjkdiejialidue2"
}
graph_config = {
    "id": "graph1",
    "name": "Reading books",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# /v1/users/<username>/graphs/<graphID>
# # Posting to the graph the quantity and date of your habit
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
date = datetime(year=2022, month=3, day=23)
# today = datetime.now()
pixel_creation_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did cycle today: ")

}
post_response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_data, headers=headers)
print(post_response.text)

today = datetime.now()
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_edit_data = {
    "quantity": input("How many kilometres did you walk today: "),

}
put_response = requests.put(url=pixel_update_endpoint, json=pixel_edit_data, headers=headers)
print(put_response.text)


# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(delete_response.text    )

