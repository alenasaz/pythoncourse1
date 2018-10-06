#из 10-ой во все системы счисления
def from10toall(number,x):
    f=""
    while number>0:
        new_num=number%x
        f+=str(new_num)
        number//=x
    print(f)
from10toall(205,7)

def from2to10(number):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*2**step
        step -= 1
    print(number1)
from2to10('10001')

def from16to10(number):
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
        print("Из 16 в 10:", number1)
from16to10('A1')

def from16to2(number):
    number1 = 0
    for i in number:
        if i=='A':
            number1 ='1010'
        elif i=='B':
            number1+='1011'
        elif i=='C':
            number1 += '1100'
        elif i=='D':
            number1 += '1101'
        elif i=='E':
            number1 += '1110'
        elif i=='F':
            number1 += '1111'
        elif i=='9':
            number1 += '1001'
        elif i=='8':
            number1 += '1000'
        elif i=='7':
            number1 += '0111'
        elif i=='6':
            number1 += '0110'
        elif i=='5':
            number1 += '0101'
        elif i=='4':
            number1 += '0100'
        elif i=='3':
            number1 += '0011'
        elif i=='2':
            number1 += '0010'
        elif i=='1':
            number1 += '0001'
        elif i=='0':
            number1 += '0000'
    print(number1)
from16to2('ABC1')


def from2to16(number):
    number1=0
    step=len(number)-1
    for i in number:
        number1+=int(i)*2**step
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
from2to16('0101011')
from2to16('1010010')
