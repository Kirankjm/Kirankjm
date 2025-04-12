ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
print(ep1)
# ep1.clear()
ep1.pop(122)
ep1.popitem()
# del ep1[122]
print(ep1) 

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'join': 'berhampur university'}
info.pop('age')
info.update({ 'join':"bu"})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003 , 'omg': 'icey'}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['eligible']
#del info
print(info)