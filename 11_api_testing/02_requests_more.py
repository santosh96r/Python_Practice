import json
import requests

def fetch_random_user_details():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    try:
        response = requests.get(url,timeout=10)     #str
        data  = response.json()   #dict

        data_json = json.dumps(data, indent = 4 )
        # print(data_json)


        with open("random_user.json", "w") as f :
            f.write(data_json)

    except Exception as e :
        print(e)

    finally :
        with open("random_user.json", "r") as f :
            print(f.read())


fetch_random_user_details()