# def func(x):
#     return x **2
#
# call = func(5)
# print(call)
# print(func(10))

# def func(x=3):
#     return x ** 3
#
# print(func(5))

# def func(word, freq = 3 ):
#
#     return word * freq
#
# print(func("sk", 2))



#===============================

# class Car(object):
#     def __init__(self, make, model , year , condition, kms):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.kms = kms
#
#     def display(self, showAll):
#         if showAll :
#             print("This car is a %s, %s from %s , It is %s and has driven for %s " %(self.make, self.model, self.year, self.condition, self.kms ))
#
#         else :
#             print("check which details you want ")
#
# c1 = Car("Reno", "duster", 2012, "New", 1200)
# print(c1.display(True))


#===================================

class Person:
    population = 50
    def __init__(self, name , age ):
        self.name = name
        self.age = age
    @classmethod
    def getpopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

p1 = Person("san" , 25)
# print(p1.getpopulation())

# print(Person.getpopulation())

print(Person.isAdult(18))