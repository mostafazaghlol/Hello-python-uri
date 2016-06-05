count=0
avg=0
for i in range(0,6):
    x=float(input())
    if(x>0):
        count=count+1
        avg=avg+x
avg=avg/count
print(count,"valores positivos")
print(avg)