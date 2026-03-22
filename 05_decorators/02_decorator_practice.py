# # decorator is a wrapper function used to modify/extend any existing functions behavior with out changing its original code
# import time
# def wrapper(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         print("inner function started ")
#         result = func(*args, **kwargs)
#         print("inner function completed ")
#         return result
#     return inner
#
# @wrapper
# def div_of_num(a,b):
#     if a > b :
#         return a / b
#     if b == 0 :
#         return "division with 0 not possible "
#     else :
#         a,b = b , a
#         return a / b
# print(div_of_num(20,5))



def wrapper(func):
    def inner(*args, **kwargs):
        print("inner func started ")
        result = func(*args, **kwargs)
        print(result)
        print("inner function completed ")
        # return result
    return inner

@wrapper
def find_div_of_nums(a,b):
    if a > b :
        return a / b
    else :
        a,b = b,a
        return a /b

print(find_div_of_nums(10,2))

