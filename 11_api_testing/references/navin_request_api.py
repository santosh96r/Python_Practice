import requests
import json
import random
import string



# ------ base url
base_url = "https://gorest.co.in"

# ------  AuthToken
auth_token = "Bearer 551c8dfe92d1bae24f3f60ea3e73ab7614e9c4bbbecc38e4cf60867df9a7ada0"

# -------- GET request
def get_users():
    url = base_url + "/public/v2/users/8402102"
    headers = {"Authorization": auth_token}

    response = requests.get(url, headers = headers)
    assert response.status_code == 200

    data = response.json()

    data_json = json.dumps(data, indent=4)
    return data_json


# ------ POST request
def create_user():
    url = base_url + "/public/v2/users"

    headers = {"Authorization" : auth_token}
    body = {
        "name": "Santosh Dravid",
        "email": "SantoshDravid8856@gyahoo.com",
        "gender": "female",
        "status": "active"
    }

    response = requests.post(url, json=body, headers = headers) # str
    data = response.json() # dct

    data_json = json.dumps(data, indent = 2 )
    return data_json

# ------ PUT request

def update_data(user_id):
    url = base_url + "/public/v2/users/" + f"{user_id}"
    headers = {"Authorization": auth_token}

    body = {
        "name": "Rahul Dravid",
        "email": "RahulDravid88566@gyahoo.com",
        "gender": "male",
        "status": "active"
    }

    response = requests.put(url , json= body, headers=headers)
    assert response.status_code == 200
    print(response.status_code)
    data_dct = response.json()
    print(data_dct)
    data_json = json.dumps(data_dct, indent = 2 )

    return data_json

# ------ DELETE request

def remove_user(user_id):
    url = base_url + "/public/v2/users/" + f"{user_id}"

    headers = {"Authorization": auth_token}

    response = requests.delete(url, headers=headers)
    print(response.status_code)
    assert response.status_code == 204

    print(f"{user_id} is deleted from DB ")

#call
# print(get_users())
print(create_user())
# print(update_data(8402102))
# remove_user(8402102)
