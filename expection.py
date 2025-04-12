a=input("enter the number")
print(f"the multiplication of {a} is",{a})

try:
 for i in range(1,10):
    print(f"int{a} x {i} = {int(a)*i}")
except:
    print("worong input")
    
print("Some imp lines of code")
print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")
  
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
  
  