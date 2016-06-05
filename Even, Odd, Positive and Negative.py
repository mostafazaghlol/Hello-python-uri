counteven=0
countodd=0
Positive=0
Negative=0
for i in range(0,5):
    x=int(input())
    if(x>0):
        Positive=Positive+1
    if(x<0):
        Negative=Negative+1
    if(x%2==0):
        counteven=counteven+1
    else:
        countodd=countodd+1
print(counteven,"valor(es) par(es)")
print(countodd,"valor(es) impar(es)")
print(Positive,"valor(es) positivo(s)")
print(Negative,"valor(es) negativo(s)")
