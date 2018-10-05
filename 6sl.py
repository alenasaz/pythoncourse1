def diff_types_all(N):
    N1=(N+2)*2
    dictor2={str(i):i for i in range(N1)}
    dictor={str(3*(i+1)):i+1 for i in range(N1)}
    z=dictor2.update(dictor)
    print("Продублированный словарь:",dictor2)
    dictor1={str(i):i for i in dictor2 if int(i)%3==1}
    print("Деление на 3:",dictor1)
    dictor4={str(i):i for i in dictor2}
    print(dictor4)
    #print(dictor4.values()[0:round(len(dictor4)/3)])
diff_types_all(3)