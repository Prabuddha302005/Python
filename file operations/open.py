# file = open("datatypes.py", "r")
# print(file)

# file = open("my.txt", "w")
# file.write("Writing in a file using file methods")


myfile = "file operations/my.txt"
file2 = "file1.txt"
with open(myfile, 'r')as file_1:

 read = file_1.read()

with open(file2, 'w')as file_2:
 file_2.write(read)

print(f"Copied {myfile} to {file2} successfully")

