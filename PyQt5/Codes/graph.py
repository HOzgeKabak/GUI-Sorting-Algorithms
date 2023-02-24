import numpy
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random

class MatplotlibWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("hw_gui.ui",self)


        self.pushButton_2.clicked.connect(self.update_graph)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self):
        A=[]
        B=[]
        for i in range(5):
            value = numpy.random.randint(0, 100)
            B.append(value)
        print("B",B)
        s=1
        for j in range(len(B)):

            A.append(s)
            s=s+1
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.bar(A,B)
        self.MplWidget.canvas.axes.bar(A,B)
        self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
