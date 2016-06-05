import math
a,b,c=map(float,input().split())
if(a==0 or (math.pow(b,2)-(4*a*c))<0 ):
    print("Impossivel calcular")
else:
    R1=((-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a))
    R2=((-b-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a))
    print("R1 = "+"{0:.5f}".format(R1))
    print("R2 = "+"{0:.5f}".format(R2))


