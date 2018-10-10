def fib1(n=0):
    list1=[1,1]
    for i in range(1,n):
        list1.append(list1[i]+list1[i-1])
    print(list1)
print("Фибоначи:")
print(fib1(10))
#task2(for)
def fib2(n=0):
    list1=[1,1,1]
    for i in range(2,n):
        list1.append(list1[i]+list1[i-1]+list1[i-2])
    print(list1)
print("Фибоначи из трех :")
print(fib2(10))
#task3(for)
def kvadrat3(srart, end, t=[]):
    for n in range(srart,end,2):
        t.append(n**2)
    print("Квадраты нечетных чисел",t)
kvadrat3(1,10)
#task4(for)
def fun4(a,b,i=0):
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
fun4(10,20)
#task5(for)
def sumandmult5(a,b,sum=0,mult=1):
    for i in range(a,b):
        sum=+i
        mult*=i
    print("Cумма:",sum,"Произведение:",mult)
sumandmult5(3,7)
#task6(for)
def unknown6(a,b,i=0,t=[],t1=[]):
    t=[i for i in range(a,b) if i%2==0]
    t1=[i for i in range(a,b) if i%2!=0]
    print("Четные:",t,"Нечетные:",t1)
unknown6(a=3,b=11)

def sortirovka7(listochek,t=[],t1=[]):
    t=[i for i in listochek if i>=0]
    t1=[i for i in listochek if i<0]
    print(t,t1)
sortirovka7(listochek=[1,-1,2,3,6,7,8,-100,-14,-0])
