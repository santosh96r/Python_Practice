import json
import requests

# load method in JSON will load a file
# loads method in JSON will load a string

# dumps method will convert a dict into a JSON string
# dump method will convert a dict into a JSON file


try :
    with open("random_user.json") as f :
        print(type(f))
        # print(type(f.read()))
        data = json.load(f)
        #
        print(type(data))
        d1 = data["data"]["login"]
        with open("test.json", "w") as f1 :
            json.dump(d1, f1, indent = 2 )


        # for key, val in data["data"]["login"].items():
        #     print(key, val)

except Exception as e :
    print(e)

