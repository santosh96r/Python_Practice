import time

def cache(func):
    cache_mem = {}
    print(cache_mem)
    def wrapper(*args):
        if args in cache_mem :
            return cache_mem[args]
        result = func(*args)
        cache_mem[args] = result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a * b

print(long_running_func(4,5))
print(long_running_func(4,5))

