

l1 = [1,2,3,4]

# def func(x):
#     for i in x :
#         print(f"{i} ** 2 = {i**2}")
#
# print(func(l1))

# ==============================
l1 = [1,2,3,4, 5]
def func(x):
    return x ** 2

# l2 = []
# for i in l1 :
#     l2.append(func(i))
#
# print(l2)
#
# l3 = list(map((lambda x : x ** 2 ), l1))
# print(l3)

# l4 = list(map((lambda x : x > 2), l1))
l4 = list(filter((lambda x : x > 2), l1))
print(l4)


a = lambda x : x ** 2

