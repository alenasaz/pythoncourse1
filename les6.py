import numpy as np
def fun1():
    ran_massive=np.random.randint(0, 100, (4, 4))
    print(ran_massive)
fun1()

def fun2():
    a = np.array([1, 2, 3,7,100])
    print("Среднее:", np.average(a))
fun2()
#стандартное отклонение
def std3():
    print("Отклонение:", np.std(np.array([1, 2, 3,7,100])))
std3()
#уравнение
def equ4():
    x=np.array([[3, 1], [1, 2]])
    c=np.array([9, 8])
    print(np.linalg.solve(x, c))
equ4()
