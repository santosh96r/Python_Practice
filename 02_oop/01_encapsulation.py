import os
import sys
import time

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary
#
#     def show(self):
#         print(f"name of Employee {self.name} adn salary is {self._salary}")
#
#     def get_salary(self):
#         print(f"salary is {self._salary}")
#
# e1 = Employee("skr", "10000")
#
# # print(e1.show())
#
# print(e1.name)
# # print(e1.__salary)
# print(e1.get_salary())


# class Company:
#     def __init__(self, name , location, branch_code):
#         self.name = name
#         self.location = location
#         self.__branch_code = branch_code
#
#     def show(self, branch):
#         print(f"Name of company : {self.name} \nLocation : {self.location} \nBranch : {branch}")
#
#     def bcode(self):
#         print(f"Branch_code : {self.__branch_code}")
#
# class Employee(Company):
#     def __init__(self,name , location ,branch_code, ename, salary, age ):
#         super().__init__(name, location, branch_code)
#         self.ename = ename
#         self._salary = salary
#         self.__age= age
#
#     def elligibility(self):
#         if self.__age > 18 :
#             print(f"Ok for CC application ")
#         else :
#             print("Try after age above 18")
#     def show(self):
#         print(f"Branch_code : {self.__branch_code}")
#
# C1 = Company("RNTBCI", "Chennai", 55)
#
# # print(C1.show("BB"))

# c2 = Employee("LG", "CHennai",10, "Ricky", 1200, 21)
# # print(c2._salary)
# # # print(c2.__age)
# # print(c2.elligibility())
#
# # print(c2._branch_code)
# # print(c2.show())
# print(C1.bcode())


# ===================================================================================
#====================================================================================

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount  # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()  # Accessing protected method
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()  # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)  # Uses both methods internally