# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5)) #10
print(cube(3))   #27
print(avg(3, 5, 10))  #6.0
print(appl(lambda x: x * x , 2)) #10
print(appl(lambda x: x * 6 , 2)) #18


# Example usage
double = lambda x: x * 2
result = appl(double, 5)
print(result)  # Output will be 16

# Function to double the input
def double(x):
  return x * 2

# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
multy = lambda x, y: x * y
outing=int(multy(4,6))
print(outing)   #result = int(double(5))
# Lambda function to calculate the product of two numbers,
# with additional print statement
evolve = lambda x, y: print(f'{x} * {y} = {x * y}')
print(str(evolve))