

# ===============Exception try, except block
#
# try :
#     result = 1/0
#     a = b
#
# # except :
# #     print("The variables has not beend assigned ")
#
# except ZeroDivisionError as ex :
#     print(ex)
#     print("change the denominator ")
#
# except NameError as ex :
#     print(ex)
#
# except Exception as e :
#     print(e)
#     print("exception is raised so check the logic again ")

# try:
#     print([h]/"k")
#
# except NameError as ex :
#     print(ex)
#
# except ZeroDivisionError as ex :
#     print(ex)
#     print("update the denominator ")
#
# except Exception as ex :
#     print(ex)

# ================ try , except , else ===========================

# =============== TRY --> Except --> Else --> FInally ===============

# try :
#     num = int(input("Enter a number : "))
#     result = 10/num
#
# except ValueError as ex :
#     print(ex)
# except ZeroDivisionError as ex :
#     print(ex)
#     print("update denominator ")
# except Exception as ex :
#     print(ex)
# else :
#     print("The result is {}".format(result))
# finally :
#     print("all blocks executed properly ")

# ============ FIle Handling and Exception Handling =================

# try :
#     with open("testing.txt", "r") as f :
#         print(f.read())
# except Exception as ex :
#     print(ex)


# ======== OOPs with Exception Handling ==========================
#
# class Pollygon:
#     def __init__(self, sides):
#         self.sides = sides
#     def show(self):
#         print("sides of the item is {}".format(self.sides))
#
# class Square(Pollygon):
#     def __init(self):
#         super().__init__(4)
#
#     def show(self):
#         print()




