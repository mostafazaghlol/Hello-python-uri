a,b,c = map(int,input().split())
maiorAB=(a+b+abs(a-b))/2
maiorfinal=(maiorAB+c+abs(maiorAB-c))/2

print("{0:.0f}".format(maiorfinal),"eh o maior")