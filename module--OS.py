import os



# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']

# Create a new directory
#os.mkdir("newdir")

# Run the "ls" command and print the output
output = os.system("dir")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
print(dir(os))
# import os

# Run the "ls" command and get the output as a file-like object
f = open(r"C:\Users\USER\Desktop\pythonk\myfile.txt.txt")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()

# Open the file in read-only mode
'''f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)'''