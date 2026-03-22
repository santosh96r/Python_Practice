import json

class User :
    def __init__(self, name , age ):
        self.name = name
        self.age = age

user = User("skr", 22)

def encode_user(object):
    if isinstance(object, User):
        return {"name":object.name, "age": object.age, object.__class__.__name__:True}
    else :
        raise TypeError("Object of type User is not JSON serilaizable ")


user_json = json.dumps(user, default = encode_user)
print(user_json)