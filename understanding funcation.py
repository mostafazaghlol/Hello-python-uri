def Order(iten="1"):
    if(iten=="Burger"):
        return 1
    elif(iten=="frensh"):
        return 2
    elif(iten=="1"):
        return 3
type=input("Enter your staff")
result=Order()
if(result==1):
    print("the check is 5.0 Dollors")
elif(result==3):
    print("the check is 15.0 Dollors")