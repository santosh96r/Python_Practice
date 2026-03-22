import requests
import json

# # import date

import requests

# url = "https://api.freeapi.app/api/v1/public/youtube/videos/"

# def get_user_agent():
#
#     headers = {"Accept": "application/json"}
#     response = requests.get(url, headers = headers)
#     # print(response.status_code)
#     data = response.json()
#     print(data["statusCode"] == 200)
#     details = data["data"]["data"]
#     for i in range(len(details)):
#         print(details[i]["title"])
#     # print(json.dumps(data, indent=4))
#
# get_user_agent()

# import requests
#
# base_url = "https://api.freeapi.app/"
# def method_post():
#
#     url = base_url + "api/v1/kitchen-sink/http-methods/post"
#     # headers = {"accept": "application/json"}
#     response = requests.post(url)
#     data = response.json()
#     print(json.dumps(data, indent = 2 ))
#
# print(method_post())
#
# # url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"
# ------ base url
base_url = "https://gorest.co.in"
base_url2 = "https://api.freeapi.app/"

# ------  AuthToken
auth_token = "Bearer 551c8dfe92d1bae24f3f60ea3e73ab7614e9c4bbbecc38e4cf60867df9a7ada0"

def get_post():
    url = base_url2 + "api/v1/users/assign-role/6489626dc265f0aa2dbb73a4"
    headers = {"Authorization": auth_token}
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    data_json = json.dumps(data, indent=4 )

    return data_json


print(get_post())
#
# def create_user():
#     url = base_url + "/public/v2/users"
#     headers = {"Authorization": auth_token}
#     body = {
#         "name": "rakesh sharma",
#         "email": "sharma_rakesh874@yahoo.co.in",
#         "gender": "male",
#         "status": "active"
#     }
#
#     response = requests.post(url, json=body, headers = headers )
#     data_dict = response.json()
#     data_json = json.dumps(data_dict, indent = 4)
#
#     return data_json
#
# # print(get_post())
# print(create_user())




