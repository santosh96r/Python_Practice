"""
03 - Strings
==============
Covers: multiline strings, slicing, methods (split, replace, strip, find, index,
        startswith), character frequency counting, removing duplicates
"""

# ==================== MULTILINE STRINGS & SPLIT ====================

# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''

# lines = multiline_string.split("\n")
# for line in lines:
#     if "people" in line:
#         print(line.replace("people", "subject"))


# ==================== SLICING ====================

# greeting = 'Hello, World!'
# print(greeting[-1:-5])       # '' (empty — can't slice backward with positive step)
# print(greeting[-1:-5:-1])    # '!dlr' (reverse slice)
# print(greeting[-5:-1])       # 'orld'


# ==================== COMMON STRING METHODS ====================

# Membership check
# if "He" in greeting:
#     print("Yes")

# strip(), startswith(), find(), index()
# my_string = "    Hello World     "
# print(my_string.strip())              # "Hello World"
# print(my_string.startswith("Hello"))  # False (leading spaces!)
# print(my_string.find("o"))            # 8
# print(my_string.index("W"))           # 10 (raises ValueError if not found)


# ==================== CHARACTER FREQUENCY ====================

# Count occurrences of each character in a string

# str1 = "aabccaabddbbacc"

# --- Approach 1: dictionary ---
# d = {}
# for ch in str1:
#     d[ch] = str1.count(ch)
# print(d)   # {'a': 5, 'b': 4, 'c': 4, 'd': 2}

# --- Approach 2: build encoded string (char + count) ---
# result = ""
# for ch in str1:
#     if ch not in result:
#         result += ch + str(str1.count(ch))
# print(result)   # "a5b4c4d2"

# --- Approach 3: same with list + join ---
# parts = []
# for ch in str1:
#     if ch not in parts:
#         parts.append(ch)
#         parts.append(str(str1.count(ch)))
# print("".join(parts))   # "a5b4c4d2"
