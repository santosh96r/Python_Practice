"""
08 - Magic / Dunder Methods
=============================
Covers: __str__, __repr__, __len__, __getitem__, __eq__, __lt__,
        __contains__, __call__, __del__
"""


# ==================== __str__ vs __repr__ ====================
# __str__  → human-readable (used by print())
# __repr__ → developer-readable (used in REPL, debugging)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} — ₹{self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


# p1 = Product("Laptop", 50000)
# p2 = Product("Phone", 20000)
# print(p1)            # Laptop — ₹50000      (__str__)
# print(repr(p1))      # Product('Laptop', 50000)  (__repr__)
# print(p1 == p2)      # False   (__eq__)
# print(p2 < p1)       # True    (__lt__)
# print(sorted([p1, p2]))  # uses __lt__ for sorting


# ==================== __len__, __getitem__, __contains__ ====================

class Playlist:
    """A custom collection that supports len(), indexing, and 'in' operator."""

    def __init__(self, name, songs=None):
        self.name = name
        self._songs = songs or []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __contains__(self, song):
        return song in self._songs

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"


# pl = Playlist("Road Trip")
# pl.add("Blinding Lights")
# pl.add("Bohemian Rhapsody")
# pl.add("Hotel California")
# print(len(pl))                    # 3
# print(pl[0])                      # Blinding Lights
# print("Hotel California" in pl)   # True
# print(pl)                         # Playlist 'Road Trip' (3 songs)


# ==================== __call__ ====================
# Makes an object callable like a function: obj()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# double = Multiplier(2)
# triple = Multiplier(3)
# print(double(10))   # 20
# print(triple(10))   # 30
# print(callable(double))  # True


# ==================== PRACTICE ====================

# 1. Create a class `Fraction` with numerator and denominator.
#    Implement __str__, __repr__, __add__, __eq__, __float__
#    Example: Fraction(1,2) + Fraction(1,3) → Fraction(5,6)
#
# 2. Create a class `HTMLElement` with tag and content.
#    Implement __str__ to return "<tag>content</tag>"
#    Implement __add__ to concatenate two elements.
#
# 3. Create a class `Stack` using a list internally.
#    Implement __len__, __getitem__, __contains__, __repr__
#    Add push() and pop() methods.
