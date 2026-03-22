"""
04 - Inheritance (Multiple & MRO)
==================================
Covers: multiple inheritance, Method Resolution Order (MRO), explicit __init__ calls
"""

# ==================== MULTIPLE INHERITANCE ====================
#
# When a class inherits from two or more parent classes:
#   class Child(Parent1, Parent2)
#
# MRO (Method Resolution Order) decides which parent's method is called first.
# Check with: ClassName.__mro__  or  ClassName.mro()

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name : {self.name}")

class Job:
    def __init__(self, salary):
        self.salary = salary
    def show(self):
        print(f"salary : {self.salary}")

class Employee(Job, Person):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Jennifer", 50000)
# emp.details()

print(emp.show())

