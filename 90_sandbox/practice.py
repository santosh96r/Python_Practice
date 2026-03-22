# class Animal:
#     legs = 4
#     def __init__(self, category, place, colour ):
#         self.category = category
#         self._place = place
#         self.__colour = colour
#
#     def show(self):
#         print(f"category : {self.category}, place : {self._place }")
#
#     @classmethod
#     def behaviour(cls):
#         print(f"This  tennds to bark ")
#
#     @staticmethod
#     def dance():
#         print("static method used ")
#
#
# a1 = Animal("bb", "kol", "ww")
#
# # print(Animal.show(a1))
# # print(Animal._place)
# # print(Animal.legs)
# # print(Animal.__colour)
# print(Animal.behaviour())
# print(Animal.dance())
#
# print(a1.dance())

#
# def outer(func):
#     def inner(*args, **kwargs):
#         print("Inner function execution started ")
#         result = func(*args, **kwargs)
#         print("Execution Completed ")
#         return result
#     return inner
#
# @outer
# def find_square():
#     for i in range(1,5):
#         print(i ** 2)
#
# print(find_square())

def find_square():
    for i in range(1,5):
        yield i ** 2

# print(list(find_square()))

# for i in find_square():
#     print(i)

# l1 = [10,15,20,25,30]
#
# d = {}
#
# for i,j in enumerate(l1, 2):
#     d[i] = j
#
# print(d)

l1 = "abcgggg"
l2 = "defff"
l3 = []

# l3 = list(zip(l1, l2))
# # print(l3)
# for i in range(min(len(l1), len(l2))):
#     l3.append(l1[i])
#     l3.append(l2[i])
#
# if len(l1) < len(l2):
#     l3.append(l2[len(l1):])
# elif len(l1) > len(l2):
#     l3.append(l1[len(l2):])
#
# print("".join(l3))

class Car:
    def __init__(self, tire, door, VIN):
        self.tire = tire
        self.door = door
        self.__VIN = VIN

    def display(self):
        print(f"Car has total {self.tire} tires and {self.door} doors ")

    def show(self):
        print(f"VIN number : {self.__VIN}")

class Sedan(Car):
    def __init__(self, tire, door , VIN, brand, model):
        super().__init__(tire, door , VIN )
        self.brand = brand
        self.model = model

    def show(self):
        print(f"car is from {self.brand} and model is {self.model}")

    def display(self):
        print(self.__VIN)

c1 = Car(4, 5, "55214")
print(c1.show())

# print(Car.show(c1))
# print(Car.door(c1))

# c2 = Sedan(3, 4, 445, "renault", "2024")
# print(c2.display())