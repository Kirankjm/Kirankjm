marks=[3,5,6,"hsrry",True,"u,miss,me",'kiran']
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#print(marks[5])#outofrange

print(marks[-3])
print(marks[len(marks)-3]) #positive index
print(marks[5-3])
print(marks[2])

if "7" in marks:
    print("im heree")
else:
    print("not me")
    
    #something is appiled on strings
    if "ha" in "harry":
        print("heee dude")
        
    print(marks)
    print(marks[1:-1])
    print(marks[1:-4])
    print(marks[1:5])    
    print(marks[1:7:2])
    print(len(marks))
    print(marks[1:7:3])
    
    lst=[i*i for i in range(9)]
    print(lst)
    lst=[i*i for i in range(9) if i%2==0]
    print(lst)