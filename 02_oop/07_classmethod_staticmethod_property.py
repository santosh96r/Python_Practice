"""
07 - Class Methods, Static Methods & Properties
=================================================
Covers: @classmethod, @staticmethod, @property, getter/setter pattern
"""


# ==================== @classmethod ====================
# Receives the CLASS (cls) as first argument, not the instance.
# Useful for factory methods or modifying class-level state.

class Employee:
    raise_percent = 1.05   # class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_percent)

    @classmethod
    def set_raise_percent(cls, percent):
        """Modify the class attribute for ALL instances."""
        cls.raise_percent = percent

    @classmethod
    def from_string(cls, emp_string):
        """Factory method — create an Employee from 'name-salary' string."""
        name, salary = emp_string.split("-")
        return cls(name, int(salary))


# e1 = Employee("Alice", 50000)
# e2 = Employee.from_string("Bob-60000")   # factory method
# Employee.set_raise_percent(1.10)
# e1.apply_raise()
# print(e1.salary)   # 55000


# ==================== @staticmethod ====================
# Does NOT receive self or cls. It's just a regular function
# that logically belongs to the class.

class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# print(MathUtils.is_even(4))      # True
# print(MathUtils.factorial(5))    # 120


# ==================== @property (getter/setter) ====================
# Lets you access methods like attributes — cleaner API.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter — accessed as temp.celsius (no parentheses)."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter — called when you do temp.celsius = value."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Read-only computed property."""
        return self._celsius * 9 / 5 + 32


# temp = Temperature(25)
# print(temp.celsius)       # 25     (getter)
# print(temp.fahrenheit)    # 77.0   (computed)
# temp.celsius = 100        # setter
# print(temp.fahrenheit)    # 212.0
# temp.celsius = -300       # raises ValueError


# ==================== PRACTICE ====================

# 1. Create a class `Circle` with radius.
#    Use @property for `area` (read-only computed property).
#    Use @classmethod `from_diameter(cls, d)` as a factory method.
#
# 2. Create a class `Config` that stores settings in a class-level dict.
#    Use @classmethod to add/update settings.
#    Use @staticmethod to validate a setting value.
#
# 3. Create a class `Password` with a private _password attribute.
#    Use @property getter that returns masked "****".
#    Use @property setter that validates min 8 chars + at least 1 digit.
