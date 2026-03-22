# num = [1,2,3,4]

# n = iter(num)

# # print(n)
# # print(list(n))
# try:
#     print(next(n))
#     print(next(n))
#     print(next(n))
#     print(next(n))
#     print(next(n))
# except StopIteration :
#     print("no more items to iterate ")

# def square(n):
#     for i in range(n):
#         # return i ** 2 
#         yield i ** 2 
    
# # print(square(4))
# print(list(square(4)))

# def fib(n):
#     a,b = 0 ,1 
#     for i in range(n):
#         yield a
#         a,b = b , a+b

# print(list(fib(10)))

# squares = list(map(lambda x : x ** 2 , [1,2,3,4]))
# print(squares)

# result = list(map(lambda x : "even" if x % 2 == 0 else "odd", (4,52,11,63,42,85,0)))
# print(result)

# result = enumerate(list(map(lambda x : "even" if x % 2 == 0 else "odd", (4,52,11,63,42,85,0))),)

# for i, j  in result:
#     print(i,j)

# s = [4,52,11,63,42,85,0]

# d = {}
# for i in s :
#     if i % 2 == 0 :
#         d[i] = "even"
#     else :
#         d[i] = "odd"

# print(d)


l1 = ["san", "tos", "mk", "ss"]

l2 = sorted(list(enumerate(l1)), key=lambda x : x[1])
print(l2)
# for i,j in l2:
#     print(i, j ) 
