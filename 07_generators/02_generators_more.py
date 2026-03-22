### PRACTICAL EXAMPLES : READING LARGE FILES 

## generators are particularly useful for reading large files because they allow you to process one line at a time 
#  without loading the entire file into memory 



# def read_large_file(filepath):
#     with open(filepath, "r") as f :
#         for line in f :
#             yield line


path = r'C:\Users\z041329\Documents\PythonPractice\07_generators\data\large_file.txt'


# try :
#     with open("path", "r") as f :
#         print(f.read())
#
# except FileNotFoundError :
#     print("Please provide a Correct File path as the current path is InCorrect ")
#
# finally :
#     with open(path, "r") as f:
#         print(f.read())

# for line in read_large_file(path):
#     print(line.strip(), end = "\n")

# print(list(read_large_file(path)))


def read_file(file_path):
    try :
        with open(file_path, "r") as f :
            for line in f :
                yield line

    except Exception as ex :
        print(ex)

print(list(read_file(path)))

