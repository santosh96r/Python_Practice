# ==============   Arithmetic operators

# print(5-6)
# print(5/2)
# print(5//2)

# print(5%2)
# print(5**2)

# =============   logical operator 

# print(5 > 2 and 3 > 4)
# print(5 > 2 or 3 > 4)   
# print(1 and 0 )
# print(1 or 0 )

#  ==============  bitwise operator 

# print(5 & 3)  # AND


# ==============   membership operator 

# print('A' in 'apple')
# print('b' not in 'apple')

# print("A" in ["apple", "banana", "mango"])

# ==============   find the sum of 3 digit number entered by user 

# num1 = int(input("enter first 3 digit number: "))
# sum = 0
# while num1 > 0:
#     digit = num1 % 10
#     sum = sum + digit
#     num1 = num1 // 10
#
# print("Sum of digits is: ", sum)

# num1 = input("Enter a number : ")
# total = 0
# for i in num1 :
#     total = total + int(i)
#
# print(total)

# num = (lambda x : x + 1)

# print(num(10))
# check_even_odd = lambda x : "even" if x % 2 == 0 else "odd"
# print(check_even_odd(25))

# num = int(input("Enter a 3 digit number : "))
# total = 0
# for i in num:
#     total += int(i)
#
# print(total)
# total = 0
# while num > 0 :
#     rem = num % 10
#     total += rem
#     num = num // 10
#
# print(total)



str1 = "aabccaabddbbacc"

# d = {}
#
# for i in str1 :
#     d[i] = str1.count(i)
#
# print(d)

# str2 = ""
# for i in str1 :
#     if i not in str2 :
#         str2 += i
#         str2 += str(str1.count(i))
#     else :
#         continue
# print(str2)

# str2 = []
# for i in str1 :
#     if i not in str2 :
#         str2.append(i)
#         str2.append(str(str1.count(i)))
#     else :
#         continue
# print("".join(str2))

#
# name = ["sa", "nt", "osh", 4]
#
# print("".join(name))

# d = {}
#
# str2 = []
# for i in str1 :
#     if i not in str2 :
#         str2.append(i)
#         str2.append(str(str1.count(i)))

# d = {}
# for i in str1 :
#     d[i] = str1.count(i)



#
# print(d)

# print(str2)
# print("".join(str2))

# for i in str1 :
#     d[i] = str1.count(i)

# print(d)

# str3 = ""
#
# for i in str1 :
#     if i not in str3 :
#         str3 = str3 + i + str(str1.count(i))
#
# print(str3)

# l5 = ["even" for i in range(40) if i % 2 == 0]

l1 = [22,15,14,54,33,22,15,39,22]

# l2 = list(map(lambda x : x ** 2 , l1))
# print(l2)

# l2 = list(filter(lambda x : x % 2 == 0, l1 ))
# print(l2)

# for key, value in enumerate(l1):
#     print(key, value)

path = r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\class_pr\practice.py"
# with open(path, "r") as f :
#     # print(f.read())
#     d = {}
#     context = f.read().split()
#     # print(context)
#     for word in context:
#         d[word] = context.count(word)
# #
# print(d)

# with open("test.txt", "w+") as f :
#     f.writelines(["My name is Skr\n", "I am from BBSR\n", "Skr is working in Bangalore"])
# with open("test.txt", "r") as f :
#     context = f.read().split()
#     # print(context)
#     d = {}
#     for word in context :
#         d[word] = context.count(word)
#     print(d)

def read_file(path):
    with open(path, "r") as f :
        for line in f.readlines():
            yield line


for line in read_file(path):
    print(line )

