dic={ "kiran": 'is a strong girl' , 
     "spoon":"material", "number":643}
print(dic["kiran"])
print(dic["number"])

dic= { 344:"lame",
     788:"kisna",
     9887 :"usman",
     6354:"jasun"}
print(dic[788])
print(type(dic))

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info.keys())
print(info.values())

print(info.items())
for key,value in info.items():
    
 print(f"the value corressponding to the key {key} is {value}")

    

for key in info.keys():
    print(f"the value corressponding to the key {key} is {info[key]}")

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
print(info.get('name'))
print(info.get('name2'))
#print(info['name2'])

