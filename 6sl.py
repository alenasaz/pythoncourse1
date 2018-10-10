def diff_types_all(N):
    N1=(N+2)*2
    dictor2={str(i):i for i in range(N1)}
    print("Созданный словарь:",dictor2)
    dictor={str(3*(i+1)):i+1 for i in range(N1)}
    z=dictor2.update(dictor)
    print("Продублированный словарь:",dictor2)
    dictor5=sorted(dictor2.values(), reverse=True)
    max1=dictor5[0]
    max2=dictor5[1]
    print("Значения, начиная со второго по убыванию числа и до предпоследнего числа: ")
    print(dictor5[dictor5.index(max2)+1:-1])
    dictor1={str(i):i for i in dictor2 if int(i)%3==1}
    print("Деление на 3:",dictor1)
    dictor4={str(i):i for i in dictor2}
    print(dictor4)
    #не получается
    print(dictor4[0:int(len(dictor4)/3)])
diff_types_all(3)
