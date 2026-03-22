"""
01 - Print, Variables, Data Types & Input
==========================================
Covers: print(), variables, id(), type(), keywords, identifiers, literals, input()
"""

# ==================== PRINT ====================

# Basic print
# print("Hello world")
# print(7.7)

# String comparison (ASCII ordering)
# print("a" > "b")   # False
# print("b" > "a")   # True

# print() with sep and end
# print("hello", 4.5, "ram", 22.5, sep="--", end="$$")
# print("hello", end=" ")
# print("world")

# Floating point edge case
# print(1e308)
# print(3.33)
# print(type(3.33))


# ==================== VARIABLES & MEMORY ====================

# Variables reference objects — assigning b = a makes both point to the same object
# a = 10
# print(a)
# b = a
# print(id(a))   # same id
# print(id(b))   # same id (small int caching)

# Multiple assignment
# a, b, c = 10, 20, 30
# print(a)


# ==================== COMPILATION vs INTERPRETATION ====================

# Python is both compiled and interpreted:
#   - Compilation: source code → bytecode (.pyc) via the compiler
#   - Interpretation: bytecode executed line-by-line by the PVM (Python Virtual Machine)
#   - CPython is the default C-language implementation of the Python interpreter


# ==================== KEYWORDS & IDENTIFIERS ====================

# Keywords: reserved words with special meaning
#   if, else, elif, for, while, def, return, import, as, from, lambda,
#   try, except, finally, with, yield, raise, global, nonlocal,
#   assert, pass, break, continue, is, in, not, and, or, del

# Identifiers: names given to variables, functions, classes, modules
#   Rules:
#     - Must start with a letter (a-z, A-Z) or underscore (_)
#     - Can contain letters, digits (0-9), and underscores
#     - Cannot be a keyword
#     - Case-sensitive


# ==================== INPUT ====================

# print(input("Enter your two numbers: "))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter your second number: "))
# print("Sum is: ", num1 + num2)


# ==================== LITERALS ====================

# Literals: fixed values assigned to variables
# Examples: 10 (int), 3.14 (float), "hello" (str), True (bool), None (NoneType)
