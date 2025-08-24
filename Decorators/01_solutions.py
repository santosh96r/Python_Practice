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


def outer(func):
    def inner(p,**kwargs):
        start = time.time()
        print("==" * 20)
        result = func(p,**kwargs)
        print(result)
        print(f"total time taken by {func.__name__}: ", time.time() - start )
               
        print("==" * 20)
    return inner 

# @outer
def div_num(a,b=50):
    if a > b :
        return a / b 
    else :
        a,b = b ,a 
        return a / b 
    
# div_num(5,20)
# main = outer(div_num)
# print(main(5,10))
print(outer(div_num)(5))

