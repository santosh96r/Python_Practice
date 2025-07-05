import time

def outer(func):
    def inner(*args, **kwargs):
        start = time.time()
        print("*" * 60)
        result = func(*args, **kwargs)
        time.sleep(2)
        print(f"result is {result}")
        print("Total time taken by func {} : ".format(func.__name__), time.time() - start)
        print("*" * 60)
    return inner
@outer
def find_div(a,b):
    if a > b :
        return a / b
    else :
        a,b = b , a
        return a/b

print(find_div(15,3))
