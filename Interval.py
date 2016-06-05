intr=float(input())
if(intr>=0 and intr<=25):
    print("Intervalo [0,25]")
elif(intr>25 and intr<=50):
    print("Intervalo (25,50]")
elif(intr>50 and intr<=75):
    print("Intervalo (50,75]")
elif(intr>75 and intr<=100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")