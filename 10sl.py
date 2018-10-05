def game1(number):
    your_number=0
    i=0
    choice=(input("Хотите сыграть в игру(yes/no):"))
    if choice=='yes':
        while number!=your_number and i<=10:
            i+=1
            if i>=10:
                print("Ваши попытки закончились")
                break
            your_number=(int(input("Введите Ваше число:")))
            if your_number==number:
                    print("Поздравляю, вы угадали")
                    print("Число Ваших попыток", i)
            elif your_number>number:
                    print("Ваше число больше, чем загаданное")
            elif your_number<number:
                    print("Ваше число меньше, чем загаданное")
game1(87)