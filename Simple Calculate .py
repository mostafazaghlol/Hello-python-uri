a, b, c = map(float, input().split())
a1, b1, c1 = map(float, input().split())
price=(b*c)+(b1*c1)
print("VALOR A PAGAR: R$","{0:.2f}".format(price))
