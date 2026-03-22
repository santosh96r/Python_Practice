# import time

# def outer(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         print("*" * 60)
#         result = func(*args, **kwargs)
#         time.sleep(2)
#         print(f"result is {result}")
#         print("Total time taken by func {} : ".format(func.__name__), time.time() - start)
#         print("*" * 60)
#     return inner
# @outer
# def find_div(a,b):
#     if a > b :
#         return a / b
#     else :
#         a,b = b , a
#         return a/b

# print(find_div(15,3))


import time

# def outer(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         print("==" * 20)
#         result = func(*args, **kwargs)
#         print(result)
#         print(f"total time taken by {func.__name__}: ", time.time() - start )
               
#         print("==" * 20)
#     return inner 

# # @outer
# def div_num(a,b):
#     if a > b :
#         return a / b 
#     else :
#         a,b = b ,a 
#         return a / b 
    
# # div_num(5,20)
# # main = outer(div_num)
# # print(main(5,10))
# print(outer(div_num)(5,35))


# def outer(func):
#     def inner(p,**kwargs):
#         start = time.time()
#         print("==" * 20)
#         result = func(p,**kwargs)
#         print(result)
#         print(f"total time taken by {func.__name__}: ", time.time() - start )
               
#         print("==" * 20)
#     return inner 

# # @outer
# def div_num(a,b=50):
#     if a > b :
#         return a / b 
#     else :
#         a,b = b ,a 
#         return a / b 
    
# # div_num(5,20)
# # main = outer(div_num)
# # print(main(5,10))
# print(outer(div_num)(5))

# def wrapper(func):
#     def inner(*args, **kwargs):
#         print("inner function started ")
#         print(func(*args, **kwargs))
#         print("inner function completed")
#     return inner
#
# @wrapper
# def find_dev(a,b):
#     if a > b :
#         return a /b
#     else :
#         a,b = b, a
#         return a / b
#
# print(find_dev(10,30))





import time
def wrapper(func):
    def inner(*args, **kwargs):
        print("==" * 30)
        start = time.time()
        result = func(*args, **kwargs )
        print(result)
        print(f"total time taken by {func.__name__.upper()} : {time.time() - start}")
        print("==" * 30)

    return inner


@wrapper
def find_square():
    for i in range(1,6):
        time.sleep(1)
        print(f" square of {i} : {i **2}")


find_square()
