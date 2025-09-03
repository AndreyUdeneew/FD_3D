# This is a sample Python script.
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import cv2
from tkinter import filedialog
from tkinter.filedialog import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def openRed():
    global fileNameRed
    fileNameRed = askopenfilenames(parent=window)
    imRed = cv2.imdecode(np.fromfile(fileNameRed, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    imRed = cv2.cvtColor(imRed, cv2.COLOR_BGR2RGB)
    imRed = imRed[:, :, 1]  # 2 for Nikita, 0 for Inessa
    return

def openGLED():
    global fileNameGLED
    fileNameGLED = askopenfilenames(parent=window)
    imGLED = cv2.imdecode(np.fromfile(fileNameGLED, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    imGLED = cv2.cvtColor(imGLED, cv2.COLOR_BGR2RGB)
    imGLED = imGLED[:, :, 1]  # 2 for Nikita, 0 for Inessa
    return

def openRLED():
    global fileNameRLED
    fileNameRLED = askopenfilenames(parent=window)
    imRLED = cv2.imdecode(np.fromfile(fileNameRLED, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    imRLED = cv2.cvtColor(imRLED, cv2.COLOR_BGR2RGB)
    imRLED = imRLED[:, :, 1]  # 2 for Nikita, 0 for Inessa
    return

def processing():
    global imRed, imGLED, imRLED
    fig    = plt.figure()
    ax     = fig.add_subplot(projection='3d')

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('1150x650')
    window.title("Осознанная тераностика")
    text1 = Text(width=70, height=1)  # image
    text1.grid(column=1, row=0, sticky=W)
    text2 = Text(width=70, height=1)  # image
    text2.grid(column=1, row=1, sticky=W)
    text3 = Text(width=70, height=1)  # image
    text3.grid(column=1, row=2, sticky=W)
    text4 = Text(width=15, height=1)  # image
    text4.grid(column=1, row=3, sticky=W)
    btn1 = Button(window, text="Select Red", command=openRed)
    btn1.grid(column=0, row=0, sticky=W)
    btn2 = Button(window, text="Select GLED", command=openGLED)
    btn2.grid(column=0, row=1, sticky=W)
    btn3 = Button(window, text="Select RLED", command=openRLED)
    btn3.grid(column=0, row=2, sticky=W)
    btn4 = Button(window, text="Vizualize!", command=processing)
    btn4.grid(column=0, row=3, sticky=W)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
