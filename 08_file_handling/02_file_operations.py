import os

print(os.getcwd())
#
# for folders in os.getcwd().split("\\"):
#     print(folders)

new_directory = "Package"
# print(os.listdir())
# os.mkdir("package")
print(os.listdir())
# os.rmdir("Package")

new_directory = "Package"
new_file = "file_handling_assignment_3.py"
file_path = os.path.join(os.getcwd(), new_file)
with open(file_path, "w") as f :
    print("new file created ")
if os.path.exists("file_handling_assignment_3.py"):
    print("file already exist")


