def run1(a=2,i=0):
    while a<=1000:
        a+=a**2
        i+=1
    print("Days",i)
run1()



def run2():
  sum=4
  num=1
  IsSimple=True
  day = 0
  while sum<1000:
      IsSimple = False
      while not IsSimple:
          num += 1
          IsSimple = True
          for i in range(2,sum//2):
              if num%i==0:
                  IsSimple = False
                  break
      sum += num
      print(sum, num)
      day += 1
  print("Days", day)
run2()

def run2(a=2):
    j=0
    while a<=1000:

        for i in range(1,a):
            j+=1
            if a%i==0:
                a+=a
            else:
                a+=1
    print("Простые числа",a,i)
run2()

def run3(firstday=10,i=1):
    while i<=30:
        firstday+=firstday*15/100
        i+=1
    print(firstday)
run3()

def run4(day1=10,counter_of_days=1,all_days=0):
    while day1<20 and all_days<100:
        day1+=day1*0.1
        all_days=+day1
        counter_of_days+=1
    print(counter_of_days)
run4()