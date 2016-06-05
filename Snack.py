a,b=map(int,input().split())
val=0.00
if(a==1):
    val=4.00
elif(a==2):
    val=4.50
elif(a==3):
    val=5.00
elif(a==4):
    val=2.00
elif(a==5):
    val=1.50

result=b*val
print("Total: R$","{0:.2f}".format(result))
