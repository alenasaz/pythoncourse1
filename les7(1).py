import matplotlib.pyplot as plt
import numpy as np
def plot1():
    tasks = 'Учеба', 'Работа', 'Курсы', 'Сон'
    times = [20, 10, 12, 56]
    xs = range(len(tasks))
    plt.bar([x for x in tasks], [ d * 0.9 for d in times],
            width = 0.2, color = 'pink', alpha = 0.7, label = '2016',
            zorder = 2)
    plt.show()
plot1()
def plot2():
    tasks = 'Учеба', 'Работа', 'Курсы', 'Сон'
    times = [20, 10, 12, 56]
    colors = ['pink', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)
    plt.pie(times, explode=explode, labels=tasks, colors=colors)
    plt.show()
plot2()

def plot3():
    x = np.array([i for i in range(-5, 4,2)])
    y = x + x ** 2 - 5
    plt.plot(x, y, color='magenta')
    y = 1 // x
    plt.plot(x, y, color='blue')
    y = x / (1 + abs(x))
    plt.plot(x, y, color='pink')
    plt.show()
plot3()

def plot4():
    x = np.array([i for i in range(50)])
    y = np.cos(x)
    plt.plot(x, y, color='magenta')
    y=np.sin(x)
    plt.plot(x, y, color='blue')
    y = np.tan(x)
    plt.plot(x, y, color='pink')
    y = 1//np.tan(x)
    plt.plot(x, y, color='black')
    plt.show()
plot4()

