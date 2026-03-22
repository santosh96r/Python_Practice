"""
02 - Inheritance & super()
===========================
Covers: single inheritance, super(), method overriding, isinstance/issubclass
"""

# ==================== SINGLE INHERITANCE ====================

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

    def info(self):
        print(f"I am an animal called {self.name}")


class Dog(Animal):
    """Dog inherits from Animal and adds new behavior."""

    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # call parent __init__
        self.breed = breed

    def fetch(self):
        print(f"{self.name} fetches the ball!")

    # Method overriding — same name as parent, different behavior
    def info(self):
        print(f"I am a {self.breed} dog called {self.name}")


# d = Dog("Buddy", "Labrador")
# d.speak()          # Buddy says Woof         (inherited)
# d.fetch()          # Buddy fetches the ball!  (own method)
# d.info()           # I am a Labrador dog called Buddy  (overridden)


# ==================== isinstance / issubclass ====================

# print(isinstance(d, Dog))      # True
# print(isinstance(d, Animal))   # True  (Dog IS-A Animal)
# print(issubclass(Dog, Animal)) # True


# ==================== MULTILEVEL INHERITANCE ====================

class Puppy(Dog):
    """Puppy inherits from Dog, which inherits from Animal."""

    def __init__(self, name, breed, toy):
        super().__init__(name, breed)
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


# p = Puppy("Max", "Beagle", "squeaky bone")
# p.speak()   # Max says Woof        (from Animal)
# p.fetch()   # Max fetches the ball! (from Dog)
# p.play()    # Max plays with squeaky bone (own)
# p.info()    # I am a Beagle dog called Max (from Dog — overridden)


# ==================== PRACTICE ====================

# 1. Create a class `Vehicle` with attributes: brand, speed
#    Create `ElectricCar(Vehicle)` that adds battery_capacity
#    Override a method `show_type()` → "Electric Vehicle"
#
# 2. Create a hierarchy: Shape → Circle → Sphere
#    Each level adds more specific calculations (area → surface area → volume)
#
# 3. Demonstrate that a child class can call parent's overridden method
#    using super().method_name()
