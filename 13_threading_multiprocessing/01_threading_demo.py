import os 
import time 
import threading
import sys  

# print(os.listdir())
# print(os.getcwd().replace("\\", "/"))

# def print_number():
#     for i in range(5):
#         time.sleep(1)
#         print(i)

# def print_letters(word):
#     for i in word:
#         time.sleep(1)
#         print(i)

# start_time = time.time()

# # print_number()
# # print_letters("abcde")

# # print(f"total_timeTaken = {time.time()- start_time}")

# t1 =  threading.Thread(target= print_number)
# t2 = threading.Thread(target=print_letters, args=("abcde", ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"total_timeTaken = {time.time()- start_time}")


# def print_numbers():
#     for n in range(5):
#         time.sleep(1)
#         print(f"number: {n}")

# def print_letters(word):
#     for ch in word:
#         time.sleep(1)
#         print("characters : {}".format(ch))

# start = time.time()

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters, args=("abcde", ))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"total time taken {time.time() - start}")


# import multiprocessing

# def square_of_numbers():
#     for i in range(1, 6):
#         time.sleep(1)
#         print(f"square of {i} : {i * i }")

# def cube_of_number():
#     for i in range(5, 10):
#         time.sleep(1)
#         print(f"cube of {i} : {i * i * i }")

# if __name__ == "__main__":
#     start = time.time()

#     p1 = multiprocessing.Process(target= square_of_numbers)
#     p2 = multiprocessing.Process(target= cube_of_number)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(f"total time taken {time.time()- start}")

# import threading
#
# def square_of_number():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Square of {i} : {i * i}")
#
# def cube_of_number():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Square of {i} : {i**3}")
#
# if __name__ == "__main__":
#     start = time.time()
#     t1 = threading.Thread(target=square_of_number)
#     t2 = threading.Thread(target=cube_of_number)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(f"tiotal time taken : {time.time() - start}")



# import threading
#
# def find_square():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"square of {i} : {i **2}")
#
#
# def find_cube():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"cube of {i} : {i **3}")
#
# if __name__ == "__main__":
#     start = time.time()
#     t1 = threading.Thread(target=find_square)
#     t2 = threading.Thread(target=find_cube)
#
#     t1.start()
#     print("\n")
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(f"Total time taken : {time.time()-start}")


# import multiprocessing

# def find_square():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"square of {i} : {i **2}")


# def find_cube():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"cube of {i} : {i **3}")

# if __name__ == "__main__":
#     start = time.time()

#     p1 = multiprocessing.Process(target=find_square)
#     p2 = multiprocessing.Process(target=find_cube)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(f"Total time taken : {time.time() - start}")




# import threading
# import time 
# import datetime

# def find_square():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"square of {i} is {i**2}")

# def find_cube():
#     for i in range(1,6):
#         time.sleep(1)
#         print(f"cube of {i} is {i**3}")


# start = time.time()

# t1 = threading.Thread(target = find_square)
# t2 = threading.Thread(target = find_cube)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"total time taken {start - time.time()}")


#
# import multiprocessing
# import time
# import os
# import sys
#
#
# def find_square():
#     """function prints the square of the numbers """
#     for i in range(1,10):
#         time.sleep(1)
#         print(f"process id of square : {os.getpid()}")
#         print(f"square of {i} : {i**2}")
#
# def find_cube():
#     """function prints the cube of a number """
#     for i in range(1,10):
#         time.sleep(1)
#         print(f"process id for cube : {os.getpid()}")
#         print(f"cube of {i} : {i**3}")
#
# if __name__ == "__main__":
#
#     start = time.time()
#
#     m1 = multiprocessing.Process(target=find_square)
#     m2 = multiprocessing.Process(target=find_cube)
#
#     m1.start()
#     m2.start()
#
#     m1.join()
#     m2.join()
#
#     print(f"total time taken : {start - time.time()}")
#




name = "santosh kumar ragar"

new_name = []

for i in name.split():
    new_name.append(i[::-1])

print(" ".join(new_name))