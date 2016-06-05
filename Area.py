a,b,c = map(float,input().split())
pi=3.14159
TRIANGULO=0.5*a*c
circle=pi*c*c
trapezium=((0.5*a+0.5*b)*c)
square=b*b
rectangle=a*b
print("TRIANGULO: "+"{0:.3f}".format(TRIANGULO))
print("CIRCULO: "+"{0:.3f}".format(circle))
print("TRAPEZIO: "+"{0:.3f}".format(trapezium))
print("QUADRADO: "+"{0:.3f}".format(square))
print("RETANGULO: "+"{0:.3f}".format(rectangle))

