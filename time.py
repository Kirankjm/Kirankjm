import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%m')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour = int(input("enter hour"))
print(hour)

if(hour>=0 and hour<12):
    print("good mrng mam")
if(hour>=12 and hour<17): 
      print("gd afternoon sir") 
if(hour>=17 and hour<0):
           print("gd night dude")