letter="hey my name is {1} and iam from {0}"
country='india' 
name='kiran'
print(letter.format(country,name))
print(letter.format(name,country))
print(f"hey myself {name} and iam from {country}")
print(f"hey myself {{name}} and iam from {{country}}")
price =78.999999
txt = f"for only {price: .2f} dollars!"
print(txt)
#print(txt.format(print =78.999999))
print((f'{2* 43}'))
print(type(f'{2* 43}'))