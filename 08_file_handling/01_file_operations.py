with open("data/example.txt", "w") as f :
    f.write("Hello, How are you \n")
    f.write("Santosh is my name ")

# with open("data/example.txt", "w") as f :
#     f.write("Am learning file handling in python ")

with open("data/example.txt", "a") as f :
    f.write("\n am from bhubaneswar ")

# with open("data/example.txt", "r") as f :
    # print(f.read())
    # print(f.readline())
    # print(f)
    # print(type(f))
    # for line in f:
    #     print(line)

lines = ["am currently working on SDV \n", "in RNTBCI \n", "in Automation"]
with open("data/example.txt", "a") as f :
    f.writelines(lines)

# with open("data/example.txt", "r") as f :
#     print(f.read())

with open("data/example2.txt", "r") as f :
    result = f.readlines()
    with open("data/example.txt", "a") as f1:
        f1.writelines(result)
        # print(f.read())
    # print(result)
# print(result)

with open("data/example.txt", "r") as f :
    d = {}
    words = f.read()
    # print(type(f.read()))
    # lines = f.readlines()
    # for line in lines :
    #     print(line.strip())
    for word in words.split():
        d[word] = words.count(word)
        # print(d)

print(d)

