

# C. Orders nested by customer -> order -> line items
orders = {
    "CUST1001": {
        "O-001": {"status": "shipped", "items": [{"sku": "P01", "qty": 2, "price": 499.0},
                                                 {"sku": "P02", "qty": 1, "price": 1299.0}]},
        "O-002": {"status": "pending", "items": [{"sku": "P03", "qty": 1, "price": 3499.0}]}
    },
    "CUST1002": {
        "O-003": {"status": "delivered", "items": [{"sku": "P02", "qty": 3, "price": 1199.0}]}
    }
}

result  = []
for key, value in orders.items():
    for order, status in value.items():
        result.append(key, order)
print(result)
# for k in orders.keys():
#     for p in orders[k].keys():
#         status = orders[k][p]["status"]
#         order_id = p
#         cust_id = k
#         l = (cust_id, order_id, status)
#         s.append(l)
# print(s)


# D. Config tree with overrides
config = {
    "defaults": {
        "theme": {"mode": "light", "accent": "blue"},
        "features": {"beta": False, "logs": {"level": "INFO", "dest": "stdout"}}
    },
    "env": {
        "prod": {"features": {"beta": False, "logs": {"level": "WARN"}}},
        "dev": {"theme": {"mode": "dark"}, "features": {"beta": True}}
    }
}



# for id in company["Engineering"].keys():
#     print(id)

# if company["HR"]["H001"] :
#     print(company["HR"].keys())


company = {
    "Engineering": {
        "E101": {"name": "Asha", "level": "SDE2", "skills": ["Python", "AWS"], "salary": 18_50_000},
        "E102": {"name": "Irfan", "level": "SDE1", "skills": ["Go", "Kubernetes"], "salary": 12_25_000},
    },
    "Sales": {
        "S201": {"name": "Meera", "region": "South", "quota": 1.2, "closed": 1.05},
        "S202": {"name": "Vikram", "region": "West", "quota": 1.0, "closed": 0.8},
    },
    "HR": {}
}

# Sum course hours
# For each course in courses, compute the total hours across modules. Return a dict {course_id: total_hours}.



# Increase Sales quota for S202 by +0.1 only if region == "West".
# d = company["Sales"]
# for k,v in d.items():
#     if d[k]["region"] == "West":
#         d[k]["quota"] += 0.1
# print(d)
# count = 0
# List all unique skills in Engineering
# Output a sorted list of unique skills from all engineers’ skills.

# l1 = []
# s = company["Engineering"]
# for key, value in s.items():
#     l1.extend(s[key]["skills"])
# print(l1)

# print(company.get("Engineering"))
# for department in company.keys():
#     # print(type(department))
#     count = count + len(company[department].keys())
#
# print(count)
#
# company["HR"] =  {
#     "H301":{
#     "name":"Ritu",
#     "level":"HRBP"
#     }
# }
# print(company["HR"])

# ===========================================================================================

# B. Courses, modules & students
courses = {
    "DSA101": {
        "title": "Data Structures",
        "modules": {
            "M1": {"name": "Arrays", "hours": 6, "students": {"st01": 82, "st02": 91}},
            "M2": {"name": "Trees", "hours": 8, "students": {"st01": 76, "st02": 88}},
        }
    },
    "ML201": {
        "title": "Intro to ML",
        "modules": {
            "M1": {"name": "Linear Models", "hours": 7, "students": {"st02": 79}},
            "M2": {"name": "Trees", "hours": 7, "students": {"st02":55}},
        }
    }
}

# d = {}
# summ = 0
# for course in courses.values():
#     for module in course["modules"].values():
#             # sum += module["hours"]
#             summ += module.get("hours")
# print(summ)
# Find best score for st01 across all modules/courses
# Return the max score achieved by "st01".
l = []
# for course in courses.values():
#     # print(courses)
#     for modules in course["modules"].values():
#         # if "st01" in modules["students"]:
#         #     l.append(modules["students"]["st01"])
#         # l.append(modules["students"]["st01"])
#         l.append(modules["students"]["st02"])
# print(l)

# for k,v in courses.items():
#     for j in courses[k]["modules"].keys() :
#         (print(courses[k]["modules"][j]["students"]["st01"]))
#         # l.append(courses[k]["modules"][j]["students"]["st01"])
#
# print(l)

# Sum course hours
# For each course in courses, compute the total hours across modules. Return a dict {course_id: total_hours}.
# d = {}
# sum = 0
# for k in courses.keys():
#     for  j in courses[k]["modules"].keys() :
#         sum = sum + int(courses[k]["modules"][j]["hours"])
#
#
# d["course_id"] = sum
# print(d)
#
# d = {"M1": {"name": "Linear Models", "hours": 7, "students": {"st02": 79}}}
#
# d1 = d["M1"]
# print(d1.get("hours"))


