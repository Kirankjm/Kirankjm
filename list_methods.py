l= [11,22,32,43,54,65,56,8,4,7,9,'k']
print(l)
l.append(16)
#l.sort(reverse=True)
l.reverse()
#print(l.index(1))
print(l.count(1))
m= l.copy()
m[0]=0
l.insert(1 , 899)
m=[900,100.1000,10001]
k= l + m
print(k)
l.extend(m)
print(l)