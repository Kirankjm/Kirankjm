x = 10 # global variable

def my_function():
  y = 5 # local variable
  print("value of y is ",y)

my_function()
print("the value of x",x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

x = 10 # global variable

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 75 # local variable
  print(y)

my_function()
print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function