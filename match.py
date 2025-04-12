x=int(input("enter the num of x"))

match x:
    case 0:
        print("iam a alfa girl")
    case 4:
        print(" iam a body builder")


    case _ if x==4:  #case with if-condition
               print(' iam a spider mam')
    case _ if x==90:
            print("iam inteelligent girl")
    case _:
            print(x ,"is in a wonderfull day")
    #case _:
            print(x ,"it is sunny day")        
                   
            