# # normal looping concept
#
# MY_LIST = [1,2,3,4,5]
#
# # for i in MY_LIST:
# #     print(i)
# # print(type(MY_LIST))
# # print(MY_LIST)
#
#
# ## ITERATOR
#
# iterator = iter(MY_LIST)
# print(type(iterator))
#
# print(iterator) # <class 'list_iterator'>
# # <list_iterator object at 0x000001F4C3A03A90>
#
# ## iterate through all the elements
# try:
#     print(next(iterator))
#     # print(next(iterator))
#     # print(next(iterator))
#     # print(next(iterator))
#     # print(next(iterator))
#     # print(next(iterator))
#     # print(next(iterator))
# except StopIteration:
#     print("No more elments to iterate ")
# # finally:
# #     print("iteration completed ")
#



l1 = [1, 2 , 3 , 4 , 5 ]
l3 = (1,2)
l2 = iter(l1)

# print(type(l2))

# print(dir(l3))
# print(len(l2))

# print(next(l1))
# print(next(l2))
# print(dir(l2))

# for i in range(len(l1)):
#     print(next(l2))


# while True :
#     try: 
#         item = next(l2)
#         print(item )

#     except StopIteration :
#         break


class MyRange:
    def __init__(self, start, end ):
        self.value = start 
        self.end = end 

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.value  >= self.end :
            raise StopIteration
        else :
            current = self.value
            self.value += 1 
            return current 
        

nums = MyRange(1, 10)

print(type(nums))
# for num in nums :
#     print(num)