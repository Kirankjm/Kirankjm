f = open(r'C:\Users\USER\Desktop\pythonk\myfile.txt' ,'r')
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)

f = open('myfile.txt', 'w')

f = open('myfile.txt', 'w')
f.write('Hello, world!')

f = open('myfile.txt', 'a')
f.write('Hello, world!')

f = open('myfile.txt', 'r')
# ... do something with the file
f.close()

#with open('myfile.txt', 'r') as f:
# ... do something with the file