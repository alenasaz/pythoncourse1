def money1(a,x,b,y,z):
    i=0
    j=0
    if a*x+b*y<=z:
        print("Нельзя")
    elif a*x==z:
        print("Можно")
    elif b*y==z:
        print("Можно")
    else:
        i+=1
        j+=1
        for i in range(a):
            for j in range(b):
                if i*x+j*y==z:
                    print("Можно")
money1(5,4,6,7,19)
def additional2(number,count=1):
    number//=10
    while number>0:
        number//=10
        count+=1
    print(count)
additional2(12)

#палиндром-она одинаково читается слева направо и справа налево
def palindrom3(stroka):
    a=stroka[::-1]
    if stroka==a:
        print("Да, является")
    else:
        print("Нет, не является")
palindrom3('Капуста')

def findwoef4(str, strinword, newstr):
    length=len(strinword)
    while str.find(strinword)>0:
        indexofword=str.find(strinword)
        str=str[:indexofword]+newstr+str[indexofword+length:]
    print(str)
findwoef4("Привет завтра вчера пока сегодня","сегодня","нет")
