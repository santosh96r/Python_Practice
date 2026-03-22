"""
05 - Loops, Comprehensions & Small Problems
=============================================
Covers: while loops, for loops, list comprehension, enumerate, digit-sum problem
"""

# ==================== SUM OF DIGITS (while loop) ====================

# num = int(input("Enter a 3-digit number: "))
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
# print("Sum of digits:", total)


# ==================== SUM OF DIGITS (for loop over string) ====================

# num_str = input("Enter a number: ")
# total = 0
# for ch in num_str:
#     total += int(ch)
# print("Sum of digits:", total)


# ==================== QUICK LAMBDA (even/odd) ====================

# check_even_odd = lambda x: "even" if x % 2 == 0 else "odd"
# print(check_even_odd(25))   # odd


# ==================== LIST COMPREHENSION ====================

# Even numbers from 0 to 39
# evens = [i for i in range(40) if i % 2 == 0]
# print(evens)


# ==================== ENUMERATE ====================

# l1 = [22, 15, 14, 54, 33, 22, 15, 39, 22]
# for index, value in enumerate(l1):
#     print(index, value)


# ==================== MUTABLE vs IMMUTABLE ====================

# Lists are mutable — both variables share the same object
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)   # [1, 2, 3, 4]  — a is also changed!

# Strings are immutable — reassignment creates a new object
# c = "test"
# d = c
# d = d + "_automation"
# print(c)   # "test"  — c is unchanged
