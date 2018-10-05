def fib1(n):
    seq1=1
    seq2=1
    number=2
    sum1=0
    while number<n:
        sum1=seq1+seq2
        seq1=seq2
        seq2=sum1
        number+=1
    return sum1
print("Фибоначи:")
print(fib1(5))
#task2(for)
def fib2(n):
    seq1=1
    seq2=1
    seq3=3
    number=2
    sum1=0
    while number<n:
        sum1=seq1+seq2+seq3
        seq1=seq2
        seq2=seq3
        seq3=sum1
        number+=1
    return sum1
print("Фибоначи из трех :")
print(fib2(4))
#task3(for)
def kvadrat3(t=[]):
    for n in range(0,10):
        if n%2!=0:
            t.append(n**2)
    print("Квадраты нечетных чисел",t)
kvadrat3()
#task4(for)
a=10
b=20
i=0
s=''
s1=''
for i in range(a):
    if i==0 or i==a-1:
        for j in range(b):
            print('*',end='')
    else:
        print('*',end='')
        for j in range(1,b-1):
            print(' ',end='')
        print('*',end='')
    print()
#task5(for)
a=3
b=7
sum=0
mult=1
i=0
def sumandmult5(a,b,sum=0,mult=1):
    for i in range(a,b):
        sum=+i
        mult*=i
    print("Cумма:",sum,"Произведение:",mult)
sumandmult5(3,7)
#task6(for)
def unknown6(a,b,i=0,t=[],t1=[]):
    for i in range(a,b):
        if i%2==0:
            t.append(i)
        else:
            t1.append(i)
    print("Четные:",t,"Нечетные:",t1)
unknown6(a=3,b=11)

def sortirovka7(listochek,t=[],t1=[]):
    for i in listochek:
        if i>=0:
            t.append(i)
        else:
            t1.append(i)
    print(t,t1)
sortirovka7(listochek=[1,-1,2,3,6,7,8,-100,-14,-0])