print ('welcome to the tip calculator')
bill = int(input('enter the total bill'))
tip = int(input('enter the tip u want to give...10 , 20 , 25 ?'))
people = int(input('enter the total persons that to be spllited'))
#calculations
#tip_amount = bill * (tip / 100)
total_bill = tip + bill
amt_per_person = float(total_bill / people)
print(f'total bill is {total_bill} and each person should paid {amt_per_person} ')

#calculations 2 in the terms of tip-percentage
tip_amount = bill * (tip / 100)
total_bill2 = tip_amount + bill
amt_per_person2 = float(total_bill2 / people)

print(f'total bill is {total_bill2} and each person should paid {amt_per_person2} ')
