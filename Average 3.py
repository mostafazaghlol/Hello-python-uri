n1,n2,n3,n4=map(float,input().split())
avg=((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print("Media:","{0:.1f}".format(avg))
if(avg>=7.0):
    print("Aluno aprovado.")
elif(avg<5.0):
    print("Aluno reprovado.")
elif(avg>=5.0 and avg<7.0):
    print("Aluno em exame.")
    n5=float(input())
    print("Nota do exame:",n5)
    avg2=(avg+n5)/2
    if(avg2>=5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:","{0:.1f}".format(avg2))