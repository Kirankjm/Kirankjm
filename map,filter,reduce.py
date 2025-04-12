# MAP 
def cube(x):
     return x>2


print(cube(2))

l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
   newl.append(cube(item))

newl = list(map(lambda x: x*x*x, l))
print(newl)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))

# FILTER
l = [1, 2, 4, 6, 4, 3]
def filter_function(a):
   return a>4
  
newnewl = list(filter(filter_function, l))
print(newnewl)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

#reduce

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sub = reduce(lambda x, y: x - y, numbers)

# Print the sum
print(sub)
