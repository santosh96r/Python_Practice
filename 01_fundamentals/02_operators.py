"""
02 - Operators
===============
Covers: Arithmetic, Logical, Bitwise, Membership operators
"""

# ==================== ARITHMETIC OPERATORS ====================

# print(5 - 6)    # -1
# print(5 / 2)    # 2.5  (true division)
# print(5 // 2)   # 2    (floor division)
# print(5 % 2)    # 1    (modulus)
# print(5 ** 2)   # 25   (exponentiation)


# ==================== LOGICAL OPERATORS ====================

# 'and' returns True only if both sides are True
# print(5 > 2 and 3 > 4)   # False

# 'or' returns True if at least one side is True
# print(5 > 2 or 3 > 4)    # True

# Short-circuit evaluation with truthy/falsy values
# print(1 and 0)   # 0   (returns first falsy, or last value)
# print(1 or 0)    # 1   (returns first truthy)


# ==================== BITWISE OPERATORS ====================

# AND: compares each bit — both must be 1
# print(5 & 3)   # 1   (binary: 101 & 011 = 001)


# ==================== MEMBERSHIP OPERATORS ====================

# 'in' checks membership in a sequence
# print('A' in 'apple')                          # False (case-sensitive)
# print('b' not in 'apple')                      # True
# print("A" in ["apple", "banana", "mango"])      # False (checks exact element)
