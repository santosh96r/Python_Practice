# special function , where "yiled" keyword is used instead of return
# it is more memory efficient
# used in mostly case of large files or infinite files
# import random
# # def random_num(count, start = 0 , end = 100):
# #     for i in range(count):
# #         yield random.randint(start, end )
# #
# # print(list(random_num(5)))
#
# def random_num(start = 0 , end = 100):
#     # for i in range(count):
#     return random.randint(start, end )
#
# print((random_num()))

#
file_path = r'C:\Users\z041329\Documents\PythonPractice\07_generators\data\large_file.txt'
# with open(file_path, "r" ) as f :
#     print(f.readlines())

# a = {'name':'santosh'}
# b = {'name':'santosh'}
#
# print(a == b)  # True
# print(a is b)  # False


data = [1, 2, 2, 3, 1, 4]


# result = list(dict.fromkeys(data))
# print(result)

# data1 = []
# for i in data :
#     if i not in data1 :
#         data1.append(i)
# print(data1)


# # employee = {"name":"skr", "age":22}
# print(employee['name'])
#
# print(employee.get("name"))
#
# print(list(employee.items()))


log = "status=PASS time=120s module=CDC"

result = dict((item.split("=")) for item in log.split())

# print(result)
    # print(item.split("="))

line = "error:timeout occurred"

# print(line.split())
# print(line.partition())


# for i in range(5):
#     if i == 2:
#         continue
#     elif i == 6:
#         break
#     print(i)


# for i in range()



