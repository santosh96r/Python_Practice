# normal looping concept 

MY_LIST = [1,2,3,4,5]

# for i in MY_LIST:
#     print(i)
# print(type(MY_LIST))
# print(MY_LIST)


## ITERATOR 

iterator = iter(MY_LIST)
print(type(iterator))

print(iterator) # <class 'list_iterator'>
# <list_iterator object at 0x000001F4C3A03A90>

## iterate through all the elements 
try:
    print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
except StopIteration:
    print("No more elments to iterate ")
# finally:
#     print("iteration completed ")