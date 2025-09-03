# This is a sample Python script.
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

fig    = plt.figure()
ax     = fig.gca(projection='3d')

x      = np.linspace(0, 1, 100)
X, Y   = np.meshgrid(x, x)
levels = np.linspace(-0.1, 0.4, 100)  #(z_min,z_max,number of contour),

a=0
b=1
c=2
Z1 = a+.1*np.sin(2*X)*np.sin(4*Y)
Z2 = b+.1*np.sin(3*X)*np.sin(4*Y)
Z3 = c+.1*np.sin(4*X)*np.sin(5*Y)

plt.contourf(X, Y,Z1, levels=a+levels,cmap=plt.get_cmap('rainbow'))
plt.contourf(X, Y,Z2, levels=b+levels,cmap=plt.get_cmap('rainbow'))
plt.contourf(X, Y,Z3, levels=c+levels,cmap=plt.get_cmap('rainbow'))

ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 2)

plt.show()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
