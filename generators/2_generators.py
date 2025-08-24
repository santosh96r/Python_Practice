### PRACTICAL EXAMPLES : READING LARGE FILES 

## generators are particularly useful for reading large files because they allow you to process one line at a time 
#  without loading the entire file into memory 



def read_large_file(filepath):
    with open(filepath, "r") as f :
        for line in f :
            yield line 


file_path = r'C:\Users\z041329\Documents\PythonPractice\Python_Practice\generators\large_file.txt'


# for line in read_large_file(file_path):
#     print(line.strip(), end = "\n")

print(list(read_large_file(file_path)))