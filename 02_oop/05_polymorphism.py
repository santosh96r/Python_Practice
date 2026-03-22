"""
05 - Polymorphism
==================
Covers: method overriding, duck typing, operator overloading
"""

# ==================== METHOD OVERRIDING (runtime polymorphism) ====================

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Same method name, different behavior depending on the object
# shapes = [Circle(5), Rectangle(4, 6)]
# for shape in shapes:
#     print(f"{shape.__class__.__name__}: area = {shape.area()}")
# Output:
#   Circle: area = 78.53975
#   Rectangle: area = 24


# ==================== DUCK TYPING ====================
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care about the type — only that the method exists.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"


def make_it_speak(thing):
    """Works with ANY object that has a speak() method — no inheritance needed."""
    print(thing.speak())


# make_it_speak(Dog())     # Woof!
# make_it_speak(Cat())     # Meow!
# make_it_speak(Robot())   # Beep boop!


# ==================== OPERATOR OVERLOADING ====================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload the + operator."""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """Overload == comparison."""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)           # Vector(4, 6)
# print(v1 == v2)     # False
# print(v1 == Vector(1, 2))  # True


# ==================== PRACTICE ====================

# 1. Create classes `Dog`, `Cat`, `Parrot` each with a `speak()` method
#    Write a function that takes a list of animals and calls speak() on each.
#
# 2. Create a `Money` class with amount and currency
#    Overload `+` to add amounts (only if same currency, else raise error)
#    Overload `>` and `==` for comparison
#
# 3. Create a `Matrix` class (2x2) and overload `+` and `*` operators
