import json

# person = {"name":"John", "age":30.0, "city":"BBSR", "HasChildren":True, "titles":["engineer", "programmer"]}

# # print(type(person))

# # print(json.dumps(person, indent = 4 ))


# # with open("test.json", "r") as f :
# #     # print(f.read())
# #     # data = f.read()
# #     d1 = json.load(f)
# # print(d1)

# # with open("test1.json", "w") as f :
# #     data = json.dumps(person, indent = 4 )
# #     f.writelines(data)

# with open("test.json", "r") as f :
#     data = json.load(f)

# print(data.keys())




import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x, indent=4))

# print(json.loads(x))

# print(x["cars"])
# for i in x["cars"]:
#     print(i.keys())









# person_json = json.dumps(person, indent = 4, sort_keys=True )
# print(person_json)

# # with open("person.json", "w+") as f :
# #     # f.writelines(person_json)
# #     json.dump(person, f , indent = 4)

#     # print(f.read())

# new_d = json.loads(person_json)
# print(new_d)


# # with open("test.json", "r") as f :
# #     d = json.load(f)
# #
# # print(d)