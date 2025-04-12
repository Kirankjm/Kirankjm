fruits = ['apple', 'banana', 'mango']
for fruit , index in enumerate(fruits):
    print(fruit,index)
    
    names = ['kiran', 'kusu', 'swagu']
    for name , index in enumerate(names,start=1):
        print(names,index)
    
    juice = ['tang', 'rasna', 'lassi']
for index, juice in enumerate(juice):
    print(f'{index+1}: {juice}')
    
    # Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
    
    # Loop over a string and print the index and value of each character
s = 'hello'
for index, s in enumerate(s):
    print(index, s)