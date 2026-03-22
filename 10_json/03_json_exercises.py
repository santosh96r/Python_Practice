import json

people_string = """
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": [
        "johnsmith@bogusemail.com",
        "john.smith@work-place.com"
      ],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
"""

# data = json.loads(people_string)
# print(type(data))
# print(data["people"][1]["emails"])
# data["people"][1]["emails"] = "skr@outlook.com"
# print(data["people"][1])


# for person in data["people"]:
#     # print(person["name"])
#     del person["phone"]
# print(data["people"][1])

# data_j = json.dumps(data, indent = 2)
# print(data_j)
# print(type(data_j))


with open("data/states.json" , "r") as f :
    data = json.load(f)
    # print(data)
    for state in data["states"] :
        # print(state["name"], state["abbreviation"])
        del state["area_codes"]

with open("data/new_state.json", "w") as f :
    json.dump(data, f, indent = 4 )
    # print(f.read())




