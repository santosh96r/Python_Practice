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

data_dict = json.loads(people_string)
# for i in data_dict["people"][0]["emails"]:
#     # print(i)
#     if i.endswith(".com") :
#         j = i.replace(".com", ".in")
#         print(j)


data_json = json.dumps(data_dict , indent= 4, sort_keys = True )

# print(type(data_dict))
# print(type(data_json))
print(data_json)



