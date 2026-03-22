import os

# def file_handling():
#     if os.path.exists("sample.txt") :
#         print("file is already available" )
#         with open("sample.txt", "r") as f :
#             return f.read()
#     else :
#         with open("sample.txt", "w") as f :
#             print("file created ")
#
# # print(file_handling())
#
# def file_handling(lines):
#     result = None
#     if os.path.exists("output.txt") :
#         print("file is already available" )
#     else :
#         with open("output.txt", "w") as f :
#             print("file created ")
#             f.writelines(lines)
#     with open("output.txt", "r") as f :
#         return f.read()

# log_lines = ["error is \n ", "Error posted on \n ", "new image found "]
# print(file_handling(log_lines))

# print(os.getcwd())
# os.chdir(r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\GitHubCopilot_trainer")
# os.mkdir("exception_handling_practice")

# if os.path.exists("demo.txt") :
#     print(os.path.join(os.getcwd(),"demo.txt" ))
# else :
#     with open("demo.txt", "w") as f :
#         print("demo file created ")

# d = {}
# with open("output.txt" , "r") as f :
#     content = f.read()
#     for i in content.strip().split() :
#         if i == " ":
#             continue
#         else :
#             d[i] = content.count(i)
#
# print(d)

# print(os.scandir())
# for i in os.scandir():
#     print(i)

# print(os.walk("top"))


# src = r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\GitHubCopilot_trainer\exception_handling_practice"
# import os
# os.chdir(r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\GitHubCopilot_trainer\exception_handling_practice")
# print(os.getcwd())
# src = "demo.txt"
# dst = r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\GitHubCopilot_trainer\FileHandling"
# os.replace(src, dst)
#


# import os
#
# src = "demo.txt"
# dst = r"C:\Users\z041329\Documents\PythonPractice\Python_Practice\GitHubCopilot_trainer\exception_handling_practice\demo.txt"
#
# os.replace(src, dst)



