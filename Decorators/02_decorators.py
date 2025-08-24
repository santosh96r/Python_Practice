## FUNCTION COPY --

# def welcome():
#     return "welcome to NLP course"

# print(welcome())

# w = welcome()
# print(w)

# w = welcome
# print(w())


## CLOUSERS 

# def main_welcome():
#     msg = "welcome"

#     def sub_welcome_method():
#         print("welcome to python course ")
#         print(msg)
#         print("please learn these concepts properly ")

#     return sub_welcome_method()

# print(main_welcome())


# def main_welcome(name):
#     msg = "welcome"

#     def sub_welcome_method():
#         print(f"hi {name} welcome to python course ")
#         print(msg)
#         print("please learn these concepts properly ")

#     return sub_welcome_method()

# print(main_welcome("skr"))


def main_welcome(func):
    msg = "welcome"

    def sub_welcome_method(num):
        print(f" welcome to python course ")
        print(msg)
        func(num)
        print("please learn these concepts properly ")

    return sub_welcome_method

# print(main_welcome(print))

def factorialss(num):
    if num == 0 or num == 1 :
        return 1 
    else :
        return num * factorialss(num-1)
    
try : 
    print(main_welcome(factorialss)(5))
except TypeError:
    print("factorialss() missing 1 required positional argument: 'num'")

    