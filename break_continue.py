for i in range(13):
    if(i==6):
        break
    print("5 x" , i+1, "=" , 5*(i))
    
    print("leave the loop")
    
    for i in range(13):
      if(i==6):
        continue
    print("5 x" , i+1, "=" , 5*(i))
    
    print("skip the loop")
    