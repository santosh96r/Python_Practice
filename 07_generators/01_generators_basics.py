# def square(n):
#     for i in range(n) :
#         return i ** 2
    
# print(square(3))

# def square(n):
#     for i in range(n) :
#         print( i ** 2 )
    
# square(3)



def square(n):
    for i in range(n) :
        yield i ** 2
    
# print(square(3))
# for i in square(4):
#     print(i)

s = square(4)
for i in s :
    print(i )

# for i in square(3):
#     print(i)


def my_generator():
    yield 1 
    yield 2 
    yield 3 

# g = my_generator()

# print(list(g))

# print(next(g))

# for i in g :
#     print(i)




import logging


