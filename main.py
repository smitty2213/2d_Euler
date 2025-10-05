import numpy as np
import matplotlib.pyplot as plt

#vector field
def velocity(x,y):
    Vx = np.sin(x ** 2 + y ** 2)
    Vy = np.cos(x ** 2 + y ** 2)
    return Vx, Vy

#array's for x and y values as they change
x_array = []
y_array = []

#inital conditions
x = 0
y = 0
dt = 5
for n in range (0,10000):
    x_array.append(x)
    y_array.append(y)
    Vx, Vy = velocity(x,y)
    x = x + Vx*dt
    y = y + Vy*dt



plt.plot(x_array, y_array)
plt.show()

    