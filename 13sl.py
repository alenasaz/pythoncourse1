def task1(number):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*8**step
        step -= 1
    x=16
    new_num=number1%x
    number1//=x
    if new_num==10:
        print(str(number1)+'A')
    elif new_num==11:
        print(str(number1)+'B')
    elif new_num==12:
        print(str(number1)+'C')
    elif new_num==13:
        print(str(number1)+'D')
    elif new_num==14:
        print(str(number1)+'E')
    elif new_num==15:
        print(str(number1)+'F')
    else:
        print(str(number1)+str(new_num))
task1('46')

def task2(number):
    number1=0
    step=len(number)-1
    for i in number:
        if i=='A':
            number1 += 10 * 16 ** step
            step -= 1
        elif i=='B':
            number1+= 11*16**step
            step -= 1
        elif i=='C':
            number1 += 12 * 16 ** step
            step-=1
        elif i=='D':
            number1 += 13 * 16 ** step
            step-=1
        elif i=='E':
            number1 += 14 * 16 ** step
            step-=1
        elif i=='F':
            number1 += 15 * 16 ** step
            step-=1
        else:
            number1 += int(i) * 16 ** step
            step -= 1
    x=8
    new_num=number1%x
    number1//=x
    print(str(number1)+str(new_num))
task2('A2')
#у меня есть из 10 во все системы в 12sl.py
#в task4 перевод из 7 и 3 в 10
def task4(number,basic):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*basic**step
        step -= 1
    print(number1)
task4('1222',3)

def task7(number):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*3**step
        step -= 1
    x=7
    new_num=number1%x
    number1//=x
    print(str(number1)+str(new_num))
task7('122')

def task8(number):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*7**step
        step -= 1
    x=3
    for i in str(number1):
        new_num=number1%x
        number1//=x
    print(str(number1)+str(new_num))
task8('652')

