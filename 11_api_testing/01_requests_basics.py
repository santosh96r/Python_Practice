import requests

def fetch_user_detail():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()

    if data["statusCode"] == 200 and "data" in data :
        userdata = data["data"]
        username = userdata['login']["username"]
        country = userdata["location"]["country"]

        print(username , country )

    else:
        raise Exception("Userdata not fetched properly ")

# fetch_user_detail()

if  __name__ == "__main__":
    fetch_user_detail()