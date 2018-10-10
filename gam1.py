import numpy as np
start=np.zeros([3,3])
print("Хотите сыграть(Yes/No)?")
choice=input()
if choice=='Yes':
    #isTrue=False
    print("Ход первого игрока. Введите две координаты от нуля до двух")
    choice1=int(input())
    choice2=int(input())
    start[choice1,choice2]=1
    print(start)
    print("Ход второго игрока. Введите две координаты от нуля до двух")
    choice3=int(input())
    choice4=int(input())
    start[choice3,choice4]=2
    print(start)
    print("Ход первого игрока. Введите две координаты от нуля до двух")
    choice5=int(input())
    choice6=int(input())
    start[choice5,choice6]=1
    print(start)
    print("Ход второго игрока. Введите две координаты от нуля до двух")
    choice7=int(input())
    choice8=int(input())
    start[choice7,choice8]=2
    print(start)
    print("Ход первого игрока. Введите две координаты от нуля до двух")
    choice9=int(input())
    choice10=int(input())
    start[choice9,choice10]=1
    print(start)
    print("Ход второго игрока. Введите две координаты от нуля до двух")
    choice11=int(input())
    choice12=int(input())
    start[choice11,choice12]=2
    print(start)
        #победа первого
    if start[0,0]==1 and start[1,1]==1 and start[2,2]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[0,0]==1 and start[0,1]==1 and start[0,2]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[1,0]==1 and start[1,1]==1 and start[1,2]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[2,0]==1 and start[2,1]==1 and start[2,2]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[0,0]==1 and start[1,0]==1 and start[2,0]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[0,1]==1 and start[1,1]==1 and start[2,1]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False
    elif start[0,2]==1 and start[1,2]==1 and start[2,2]==1:
        print("Первый игрок победил. Поздравляю")
        isTrue=False

        #победа второго
    elif start[0,0]==2 and start[1,1]==2 and start[2,2]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    elif start[0,0]==2 and start[0,1]==2 and start[0,2]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    elif start[1,0]==2 and start[1,1]==2 and start[1,2]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    elif start[2,0]==2 and start[2,1]==2 and start[2,2]==2:
        print("Второй игрок победил. Поздравляю")
    elif start[0,0]==2 and start[1,0]==2 and start[2,0]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    elif start[0,1]==2 and start[1,1]==2 and start[2,1]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    elif start[0,2]==2 and start[1,2]==2 and start[2,2]==2:
        print("Второй игрок победил. Поздравляю")
        isTrue=False
    else:
        print("Ничья")

else:
    print("До свидания")
