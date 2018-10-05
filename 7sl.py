def multstr1(number,str):
    print("Cтрока повторяется несколько раз:",number*'str')
multstr1(3,'fdgg')

def stair2(n1):
    for i in range(n1):
        print('='*i)
stair2(5)
#слайд7(задание3)
def count_letters3(str):
    i=0
    s={i:str.count(i) for i in set(str)}
    print(s)
count_letters3('Alena Sazanova')
#слайд7(задание4)
def sort_words4(list):
    list.sort(key=len)
    return list
print(sort_words4(["first", "second", "third", "fourth ", "fifth"]))
