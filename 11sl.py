def additional1(number,count=1):
    number//=10
    while number>0:
        number//=10
        count+=1
    print(count)
additional1(12)

#палиндром-она одинаково читается слева направо и справа налево
def palindrom2(stroka):
    a=stroka[::-1]
    if stroka==a:
        print("Да, является")
    else:
        print("Нет, не является")
palindrom2('Капуста')

def findwoef3(str, strinword, newstr):
    length=len(strinword)
    while str.find(strinword)>0:
        indexofword=str.find(strinword)
        str=str[:indexofword]+newstr+str[indexofword+length:]
    print(str)
findwoef3("Привет завтра вчера пока сегодня","сегодня","нет")
