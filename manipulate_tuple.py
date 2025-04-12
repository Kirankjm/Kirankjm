countries=("spain","italy","india", "england","lodon","Germany")
temp=list(countries)
print(temp)
temp.append("russia") #add items
temp.pop(3) #delete item
temp[2]="finland"  #change item
countries=tuple(temp)
print(countries)

car_name1=("Rolls-Royce","bugatti","mercedes","mcLaren")
print(car_name1)
car_india=("tata nexon","tata safari","mahindra","honda")
print(car_india)
total_cars = car_name1 + car_india
print(total_cars)
