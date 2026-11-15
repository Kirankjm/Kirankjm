print("welcome to the rollercoaster")
height = int(input("enter your height in inch"))
if height >3 :
    print("you can enjoy rollercoaster")
    age =int(input('hey, what is your age'))
    if age <= 11:
        print('plz , pay $5')
    elif age <= 18:
        print('plz, pay $7')
    else:
        print('pay $10')
else:
    print("sry guys, you come with grow older" )

print("another situation")

user_time = input(" when will u freee ,Enter a time: ")
if user_time == "2:30" or user_time == "3:30" :
    print("i am free to talk with you")
else:
    print("i'm busy dear")

