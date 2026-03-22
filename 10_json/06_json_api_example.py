import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers"

    response = requests.get(url)
    data = response.json()
    print(type(data))
    print(data["statusCode"])
    # print(data["data"]["data"])
    for i in data["data"]["data"]:
        if i["gender"] == "male":
            print(i["location"]["street"]["name"])
    # return data

print(fetch_random_user())