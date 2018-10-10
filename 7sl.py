def multstr1(number,str):
    print("Cтрока повторяется несколько раз:",number*'str')
multstr1(3,'fdgg')

def stair2(n1):
    for i in range(1,n1+1):
        print('='*i)
stair2(5)
#слайд7(задание3)
def count_letters3(str):
    i=0
    s={i:str.count(i) for i in set(str)}
    print(s)
count_letters3('Alena Sazanova')
#слайд7(задание4)
def sort_word5(str1):
    m=[str(s.lower()) for s in str1.split()]
    length=[]
    for i in m:
        length.append(len(i))
    dictionary={}
    for k in sorted(length):
        if k in dictionary:
            dictionary[k]+=1
        else:
            dictionary[k]=1
    print(dictionary)
sort_word5(input("Введите строку"))
#print(sort_word5(["first", # "second", "third", "fourth ", "fifth"]))
