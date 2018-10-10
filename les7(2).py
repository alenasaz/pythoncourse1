from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pylab
import numpy as np
fig = pyplot.figure()
ax = Axes3D(fig)

def makeData():
    x = np.arange (-10, 10, 0.1)
    y = np.arange (-10, 10, 0.1)
    xgrid,ygrid=np.meshgrid(x,y) #функция создает двумерные матрицы сеток по одномерным массивам.
    zgrid=np.sin (xgrid) * np.sin(ygrid) / (xgrid * ygrid)
    return xgrid,ygrid,zgrid
x,y,z=makeData()

ax.plot_surface(x,y,z,color='red')
pylab.show()