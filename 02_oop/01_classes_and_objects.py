"""
01 - Classes, Objects & __init__
=================================
Covers: class definition, __init__ constructor, self, instance attributes,
        instance methods, creating objects
"""

# ==================== BASIC CLASS ====================

class Car:
    """A simple Car class to demonstrate class basics."""

    def __init__(self, brand, model, year):
        """Constructor — called automatically when an object is created."""
        self.brand = brand    # instance attribute
        self.model = model
        self.year = year

    def display_info(self):
        """Instance method — operates on self (the current object)."""
        print(f"{self.year} {self.brand} {self.model}")

    def age(self, current_year=2026):
        return current_year - self.year


# --- Creating objects ---
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# car1.display_info()          # 2020 Toyota Camry
# car2.display_info()          # 2022 Honda Civic
# print(car1.age())            # 6
# print(car1.brand)            # Toyota


# ==================== CLASS vs INSTANCE ATTRIBUTES ====================

class Employee:
    """Demonstrates class-level vs instance-level attributes."""

    company = "TechCorp"   # class attribute — shared by ALL instances

    def __init__(self, name, role):
        self.name = name   # instance attribute — unique per object
        self.role = role

    def show(self):
        print(f"{self.name} ({self.role}) at {Employee.company}")


# e1 = Employee("Alice", "Developer")
# e2 = Employee("Bob", "Tester")
# e1.show()                     # Alice (Developer) at TechCorp
# e2.show()                     # Bob (Tester) at TechCorp

# Changing class attribute affects all instances
# Employee.company = "NewCorp"
# e1.show()                     # Alice (Developer) at NewCorp


# ==================== PRACTICE ====================

# 1. Create a class `Book` with attributes: title, author, pages
#    Add a method `summary()` that prints "Title by Author, Pages pages"
#
# 2. Create a class `Rectangle` with width and height
#    Add methods: area(), perimeter(), is_square()
#
# 3. Create a class `Student` with name, marks (list)
#    Add methods: average(), grade() (A/B/C/F based on average)
