import ast
import time
import webbrowser
import os
import winsound
from tkinter import filedialog

import matplotlib.pyplot as plt
from playsound import playsound
from pygame import mixer
import numpy
import tkinter as tk

import pandas as pd
from PyQt5.QtCore import QPropertyAnimation, QRect, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QDoubleValidator, QValidator, QIntValidator, QMovie
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets, QtGui
from PyQt5.QtGui import QIcon

from graph_fib import page
from dir.package.binarysearch import binarysearch
import half_array
import insertion
from hw_gui_python import Ui_MainWindow
import numpy as np
import random as rd
from dir.package.insertionSort import insertionSort
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from graph_fib import page
from qrcodes import code
from HW6 import rand_select
from dir.package.bubble_sort import bubble_sort
from dir.package.heapsort import heapsort
from dir.package.bucketsort import bucket_sort
from Merge_sort import Merge_sort
from dir.package.quicksort import quicksort
from counting import count_sort
from radixsort import radixSort
from selection import selectionSort
from Gnome import gnomeSort
from comb import combsort
from shell import shellSort

class homework(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.home_page_index=0
        #self.array_index=1
        self.sort_index=1
        self.fib_index=2
        self.binary_index=3
        self.ith_index=4
        self.matrix_mult=5
        self.comp_index=6
        self.exit_index=7
        self.show_time = 3000
        self.ui.lineEdit_control.setValidator(QIntValidator(0, 999, self))
        self.ui.actionPage_home.triggered.connect(self.go_home)
        self.ui.actionFibonacci.triggered.connect(self.fib_page)
       # self.ui.actionSelect_Array.triggered.connect(self.go_select)
        self.ui.actionSort_Array.triggered.connect(self.go_sort)
        self.ui.actionBinary_Search.triggered.connect(self.binary_page)
        self.ui.actionMatrix_Calculations.triggered.connect(self.random_matrix)
        self.ui.actionComparison.triggered.connect(self.comparison)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.enter)
        self.ui.actionIth_Smallest_Number.triggered.connect(self.ith_smallest)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.melody=self.ui.dial_sound.value()
        self.ui.pushButton_49.clicked.connect(self.guide)
        self.go_home()
    def guide(self):

        os.startfile("Report-Guide.pdf")
    def enter(self):
        name = self.ui.lineEdit_name.text()
        password = self.ui.lineEdit_password.text()
        y = 0
        s = 0



        va=0
        if self.ui.checkBox_25.isChecked() :
            if self.ui.checkBox_29.isChecked():
               if self.ui.checkBox_33.isChecked():
                   if self.ui.checkBox_32.isChecked():
                       if self.ui.checkBox_31.isChecked():
                         va=1
                       else:
                           va=0
                   else:
                       va=0
               else:
                   va=0
            else:
                va=0
        else:
            va=0

        if (name == "Ozge") and (va == 1):
            s = 1
        else:
            s = 0

        if (name=="Ozge") and (password=='12345'):
           y=1
        else:
           y=0


        if (s==1) or (y==1):
            result = int(self.ui.lineEdit_control.text())
            if result == (self.number1 + self.number2):
                #self.ui.statusbar.showMessage("Succesfull Entry", self.show_time)
                self.ui.toolBar.setEnabled(True)
                self.ui.menubar.setEnabled(True)
                self.go_sort()
            else:
                QMessageBox.warning(self, "Control", "Answer Is Wrong!")
        else:
            #self.ui.statusbar.showMessage("Name Or Password is incorrect", self.show_time)
            QMessageBox.warning(self, "Incorrect Entry", "Name Or Password Is Incorrect!")
    def go_home(self):
        self.number1 = rd.randint(0, 100)
        self.number2 = rd.randint(0, 100)
        self.ui.lineEdit_control.clear()
        self.ui.label_control.setText("{}+{} =?".format(self.number1, self.number2))
        self.ui.stackedWidget.setCurrentIndex(self.home_page_index)
        self.ui.toolBar.setEnabled(False)
        self.ui.menubar.setEnabled(False)
        self.ui.pushButton_23.setVisible(False)
        self.ui.pushButton_22.clicked.connect(self.see)
        self.ui.pushButton_23.clicked.connect(self.lock)
        self.ui.pushButton_4.clicked.connect(self.ikcu)
        self.ui.pushButton_24.clicked.connect(self.yt)
        self.ui.pushButton_25.clicked.connect(self.mail)
        self.ui.checkBox_25.setVisible(False)
        self.ui.checkBox_26.setVisible(False)
        self.ui.checkBox_27.setVisible(False)
        self.ui.checkBox_28.setVisible(False)
        self.ui.checkBox_29.setVisible(False)
        self.ui.checkBox_30.setVisible(False)
        self.ui.checkBox_31.setVisible(False)
        self.ui.checkBox_32.setVisible(False)
        self.ui.checkBox_33.setVisible(False)
        self.ui.pushButton_27.setVisible(False)
        self.ui.pushButton_26.clicked.connect(self.password)
        self.ui.pushButton_27.clicked.connect(self.pattern)
        self.ui.lineEdit_password.setVisible(True)
        self.ui.pushButton_22.setVisible(True)
        self.ui.pushButton_23.setVisible(True)
        self.ui.pushButton_26.setVisible(True)
        movie = QMovie('HOK.gif')
        self.ui.label.setMovie(movie)
        movie.start()
        self.ui.label.show()


    def pattern(self):
        self.ui.checkBox_25.setVisible(False)
        self.ui.checkBox_26.setVisible(False)
        self.ui.checkBox_27.setVisible(False)
        self.ui.checkBox_28.setVisible(False)
        self.ui.checkBox_29.setVisible(False)
        self.ui.checkBox_30.setVisible(False)
        self.ui.checkBox_31.setVisible(False)
        self.ui.checkBox_32.setVisible(False)
        self.ui.checkBox_33.setVisible(False)
        self.ui.pushButton_27.setVisible(False)
        self.ui.pushButton_26.setVisible(True)
        self.ui.lineEdit_password.setVisible(True)
        self.ui.pushButton_22.setVisible(True)
        self.ui.pushButton_23.setVisible(True)


    def password(self):
        self.ui.pushButton_26.setVisible(False)
        self.ui.lineEdit_password.setVisible(False)
        self.ui.pushButton_22.setVisible(False)
        self.ui.pushButton_23.setVisible(False)
        self.ui.checkBox_25.setVisible(True)
        self.ui.checkBox_26.setVisible(True)
        self.ui.checkBox_27.setVisible(True)
        self.ui.checkBox_28.setVisible(True)
        self.ui.checkBox_29.setVisible(True)
        self.ui.checkBox_30.setVisible(True)
        self.ui.checkBox_31.setVisible(True)
        self.ui.checkBox_32.setVisible(True)
        self.ui.checkBox_33.setVisible(True)
        self.ui.pushButton_27.setVisible(True)


    def mail(self):
        recipient = 'ozge13kbk@hotmail.com'
        webbrowser.open('mailto:?to=' + recipient , new=1)

    def yt(self):
        webbrowser.open("https://www.youtube.com/channel/UCVx9odXaosySGaDtXX96QGA")

    def ikcu(self):
        webbrowser.open("https://muh.ikcu.edu.tr/")

    def lock(self):
        self.ui.lineEdit_password.setEchoMode(2)
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.hide()

    def see(self):
        self.ui.lineEdit_password.setEchoMode(False)
        self.ui.pushButton_22.hide()
        self.ui.pushButton_23.show()

    def go_sort(self):
        self.ui.stackedWidget.setCurrentIndex(self.sort_index)

        self.ui.pushButton_2.clicked.connect(self.update_graph)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.addToolBar(NavigationToolbar(self.ui.MplWidget.canvas, self))
        self.ui.horizontalSlider.valueChanged.connect(self.visibility)
        self.ui.pushButton_insertion.clicked.connect(self.insertion)

        self.ui.pushButton_merge.clicked.connect(self.merge_app)
        self.ui.pushButton_bubble.clicked.connect(self.bubble_app)
        self.ui.pushButton_quick.clicked.connect(self.quick_app)
        self.ui.pushButton_heap.clicked.connect(self.heap_app)
        self.ui.pushButton_counting.clicked.connect(self.counting_app)
        self.ui.pushButton_radix.clicked.connect(self.radix_app)
        self.ui.pushButton_bucket.clicked.connect(self.bucket_app)
        self.ui.pushButton_shell.clicked.connect(self.shell_sort)
        self.ui.pushButton_comb.clicked.connect(self.combsort)
        self.ui.pushButton_gnome.clicked.connect(self.gnome)
        self.ui.pushButton_selection.clicked.connect(self.selection)
        self.ui.pushButton_18.clicked.connect(self.default)
        self.ui.pushButton_21.clicked.connect(self.time_func)
        self.ui.pushButton_28.clicked.connect(self.cont)
        self.ui.pushButton_29.clicked.connect(self.skip)
        self.ui.pushButton_30.clicked.connect(self.clean)
        self.ui.pushButton_31.clicked.connect(self.txt)
        self.ui.pushButton_32.clicked.connect(self.save)
        self.ui.pushButton_33.clicked.connect(self.audio)
        self.ui.pushButton_43.clicked.connect(self.your_array)
        self.ui.pushButton_44.clicked.connect(self.add_num)
        self.ui.pushButton_48.clicked.connect(self.qr)
        self.ui.pushButton_50.clicked.connect(self.nmbrs)
        self.ui.pushButton_33.setVisible(False)
        now = QtCore.QDate.currentDate()
        now_time=QtCore.QTime.currentTime()
        self.ui.dateEdit.setDate(now)
        self.ui.timeEdit.setTime(now_time)
        movie = QMovie('sorted.gif')
        self.ui.label_19.setMovie(movie)
        movie.start()

        self.ui.label_19.hide()

    def disable(self):
        self.ui.pushButton_gnome.setEnabled(False)
        self.ui.pushButton_comb.setEnabled(False)
        self.ui.pushButton_bucket.setEnabled(False)
        self.ui.pushButton_radix.setEnabled(False)
        self.ui.pushButton_counting.setEnabled(False)
        self.ui.pushButton_heap.setEnabled(False)
        self.ui.pushButton_quick.setEnabled(False)
        self.ui.pushButton_bubble.setEnabled(False)
        self.ui.pushButton_merge.setEnabled(False)
        self.ui.pushButton_insertion.setEnabled(False)
        self.ui.pushButton_selection.setEnabled(False)
        self.ui.pushButton_shell.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_18.setEnabled(False)
        self.ui.pushButton_48.setEnabled(False)
        self.ui.pushButton_43.setEnabled(False)
        self.ui.pushButton_44.setEnabled(False)
        self.ui.pushButton_50.setEnabled(False)
        self.ui.pushButton_31.setEnabled(False)
        self.ui.pushButton_32.setEnabled(False)
    def enable(self):
        self.ui.pushButton_gnome.setEnabled(True)
        self.ui.pushButton_comb.setEnabled(True)
        self.ui.pushButton_bucket.setEnabled(True)
        self.ui.pushButton_radix.setEnabled(True)
        self.ui.pushButton_counting.setEnabled(True)
        self.ui.pushButton_heap.setEnabled(True)
        self.ui.pushButton_quick.setEnabled(True)
        self.ui.pushButton_bubble.setEnabled(True)
        self.ui.pushButton_merge.setEnabled(True)
        self.ui.pushButton_insertion.setEnabled(True)
        self.ui.pushButton_selection.setEnabled(True)
        self.ui.pushButton_shell.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_18.setEnabled(True)
        self.ui.pushButton_48.setEnabled(True)
        self.ui.pushButton_43.setEnabled(True)
        self.ui.pushButton_44.setEnabled(True)
        self.ui.pushButton_50.setEnabled(True)
        self.ui.pushButton_31.setEnabled(True)
        self.ui.pushButton_32.setEnabled(True)

    def nmbrs(self):
        val= self.ui.comboBox_2.currentIndex()
        if val==0:
            self.ui.listWidget.clear()
            for i in range(len(self.B)):
                if self.B[i]%2==0:
                    a=str(self.B[i])
                    self.ui.listWidget.addItem(a)
        elif val==1:
            self.ui.listWidget.clear()
            for i in range(len(self.B)):
                if self.B[i]%2==1:
                    a=str(self.B[i])
                    self.ui.listWidget.addItem(a)
        elif val==2:
            self.ui.listWidget.clear()
            for i in range(len(self.B)):
                n=self.B[i]


                # Compute sum of terms like digit multiplied by
                # power of position
                sum = 0

                # find the sum of the cube of each digit
                temp = n
                while temp > 0:
                    digit = temp % 10
                    sum += digit ** 3
                    temp //= 10

                # display the result
                if n== sum:

                    a = str(self.B[i])
                    self.ui.listWidget.addItem(a)
        elif val == 3:
            self.ui.listWidget.clear()
            for i in range(len(self.B)):
                n = self.B[i]
                sum1 = 0
                for j in range(1, n):
                    if (n % j == 0):
                        sum1 = sum1 + j
                if (sum1 == n):
                    a = str(self.B[i])
                    self.ui.listWidget.addItem(a)
        elif val == 4:
            self.ui.listWidget.clear()

            for i in range(len(self.B)):
                # Make a copy of num and store it in variable n
                num=self.B[i]
                n = num
                rem = sum = 0
                # Calculates sum of digits
                while (num > 0):
                    rem = num % 10
                    sum = sum + rem
                    num = num // 10

                    # Checks whether the number is divisible by the sum of digits
                if (n % sum == 0):
                    a = str(self.B[i])
                    self.ui.listWidget.addItem(a)

    def qr(self):
        self.page = code()
        self.page.show()

    def alarm(self):
        val=self.ui.comboBox_3.currentIndex()
        if val==0:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        elif val==1:
            winsound.Beep(500,1000)
        elif val==2:
            playsound("Ses1.mp3")
        elif val==3:
            playsound("Ses-001.mp3")
        elif val == 4:
            playsound("Ses-002.mp3")
        elif val == 5:
            playsound("Ses-003.mp3")
        elif val == 6:
            playsound("Ses-004.mp3")
        elif val == 7:
            playsound("Ses-005.mp3")
    def audio(self):
        A=self.ui.comboBox.currentIndex()
        if A==0:
            mixer.init()
            mixer.music.load('happy.mp3')
            mixer.music.play()
        elif A==1:
            mixer.init()
            mixer.music.load('rainy.mp3')
            mixer.music.play()
        elif A==2:
            mixer.init()
            mixer.music.load('excited.mp3')
            mixer.music.play()
        elif A==3:
            mixer.init()
            mixer.music.load('emotional.mp3')
            mixer.music.play()
        elif A==4:
            mixer.init()
            mixer.music.load('curious.mp3')
            mixer.music.play()
        elif A==5:
            mixer.init()
            mixer.music.load('relax.mp3')
            mixer.music.play()
        elif A==6:
            mixer.init()
            mixer.music.load('Goodfeel.mp3')
            mixer.music.play()
        elif A==7:
            mixer.init()
            mixer.music.load('short.mp3')
            mixer.music.play()

    def save(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("xlsx file", "*.xlsx"), ("all files", "*.*")))
        df = pd.read_excel(file_path)
        self.B = df.columns
        self.B = list(self.B)

        for i in range(len(self.B)):
            self.B[i] = int(self.B[i])
        t = np.linspace(1, len(self.B), len(self.B))
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(t, self.B, color='pink', edgecolor="purple")
        self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                               ha='right',
                                               fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        self.length=len(self.B)
        self.A=t

    def txt(self):
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.asksaveasfilename(
            defaultextension="csv",
            filetypes=[("csv file", "*.csv"), ("All Files", "*.*")],
        )

        with open(filepath, "w") as output_file:
            text = str(self.B)
            text = text.strip("[")
            text = text.strip("]")
            output_file.write(text)

    def clean(self):
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
        self.ui.MplWidget.canvas.axes.axis("off")
        self.ui.MplWidget.canvas.draw()
    def skip(self):
        insertionSort(self.B)
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(self.A, self.B ,color="pink", edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        self.enable()
    def cont(self):
        global i
        self.i = int(1)
        mixer.music.unpause()
        self.buton()
    def time_func(self):
        global i
        self.i = int(0)
        mixer.music.pause()
        self.buton()

    def buton(self):
        t = 0
        while self.i == 0:
            if self.i == 1:
                if self.i == 2:
                    self.ui.MplWidget.canvas.axes.clear()  # clear graph
                    self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                    break
                break
            time.sleep(1)
            QApplication.processEvents()
            if self.i == 2:
                self.ui.MplWidget.canvas.axes.clear()  # clear graph
                self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                break
    def speed(self):
        m=self.ui.dial_max.value()
        n=self.ui.dial_mult.value()
        r=self.ui.dial_min.value()
        self.ui.vs.setMaximum(m*n)
        self.ui.vs.setMinimum(n*r)
        v=self.ui.vs.value()
        self.velocity=0.001*(100-v)
        self.ui.lcdNumber_3.display(self.velocity)
    def insertion(self):
            self.melody=self.ui.dial_sound.value()
            self.disable()
            if self.melody==0:
                #self.audio()
                self.ui.MplWidget.canvas.axes.axis('off')
                for j in range(1, len(self.B)):

                    key = self.B[j]

                    i = j - 1
                    while i >= 0 and key < self.B[i]:
                        self.B[i + 1] = self.B[i]
                        i -= 1

                        self.ui.MplWidget.canvas.axes.clear()
                        self.ui.MplWidget.canvas.axes.bar(self.A, self.B,color="pink", edgecolor="purple")

                        self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red", edgecolor="black")
                        self.ui.MplWidget.canvas.axes.bar(self.A[i + 1], self.B[i+ 1], color="red", edgecolor="black")
                        for k, v in enumerate(self.B):
                            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                               ha='right',
                                                               fontweight='bold', fontsize=8)
                        self.ui.MplWidget.canvas.axes.axis('off')
                        self.ui.MplWidget.canvas.draw()
                        self.speed()
                        QApplication.processEvents()

                    self.B[i + 1] = key
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    QApplication.processEvents()

                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.enable()
            #mixer.music.stop()
            #self.alarm()
            elif self.melody==1:
                self.audio()
                self.ui.MplWidget.canvas.axes.axis('off')
                for j in range(1, len(self.B)):

                    key = self.B[j]

                    i = j - 1
                    while i >= 0 and key < self.B[i]:
                        self.B[i + 1] = self.B[i]
                        i -= 1

                        self.ui.MplWidget.canvas.axes.clear()
                        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")

                        self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red", edgecolor="black")
                        self.ui.MplWidget.canvas.axes.bar(self.A[i + 1], self.B[i + 1], color="red", edgecolor="black")
                        for k, v in enumerate(self.B):
                            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple',
                                                               va='center',
                                                               ha='right',
                                                               fontweight='bold', fontsize=8)
                        self.ui.MplWidget.canvas.axes.axis('off')
                        self.ui.MplWidget.canvas.draw()
                        self.speed()
                        QApplication.processEvents()

                    self.B[i + 1] = key
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    QApplication.processEvents()

                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                mixer.music.stop()
                self.enable()
            elif self.melody==2:
                self.ui.MplWidget.canvas.axes.axis('off')
                for j in range(1, len(self.B)):

                    key = self.B[j]

                    i = j - 1
                    while i >= 0 and key < self.B[i]:
                        self.B[i + 1] = self.B[i]
                        i -= 1

                        self.ui.MplWidget.canvas.axes.clear()
                        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")

                        self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red", edgecolor="black")
                        self.ui.MplWidget.canvas.axes.bar(self.A[i + 1], self.B[i + 1], color="red", edgecolor="black")
                        for k, v in enumerate(self.B):
                            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple',
                                                               va='center',
                                                               ha='right',
                                                               fontweight='bold', fontsize=8)
                        self.ui.MplWidget.canvas.axes.axis('off')
                        self.ui.MplWidget.canvas.draw()
                        self.speed()
                        QApplication.processEvents()

                    self.B[i + 1] = key
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    QApplication.processEvents()


                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.alarm()
            self.enable()
    def merge_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==0:


            self.ui.MplWidget.canvas.axes.axis('off')
            array = self.B
            len_2 = len(self.B)
            t = np.linspace(1, len_2, len_2)
            half_first, half_second = half_array.half_array(array)
            half_first = insertion.insertion_sort(half_first)
            half_second = insertion.insertion_sort(half_second)
            half_first = np.append(half_first, 99999)
            half_second = np.append(half_second, 99999)
            i = 0
            j = 0
            for counter in range(0, len(array)):
                if half_first[i] <= half_second[j]:
                    array[counter] = half_first[i]
                    i = i + 1

                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[i + 1], self.B[i + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
                else:
                    array[counter] = half_second[j]
                    j = j + 1
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[j + 1], self.B[j + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()

                    QApplication.processEvents()
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink",edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                                fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()

        elif self.melody==2:
            self.ui.MplWidget.canvas.axes.axis('off')
            array = self.B
            len_2 = len(self.B)
            t = np.linspace(1, len_2, len_2)
            half_first, half_second = half_array.half_array(array)
            half_first = insertion.insertion_sort(half_first)
            half_second = insertion.insertion_sort(half_second)
            half_first = np.append(half_first, 99999)
            half_second = np.append(half_second, 99999)
            i = 0
            j = 0
            for counter in range(0, len(array)):
                if half_first[i] <= half_second[j]:
                    array[counter] = half_first[i]
                    i = i + 1

                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[i + 1], self.B[i + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
                else:
                    array[counter] = half_second[j]
                    j = j + 1
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[j + 1], self.B[j + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()

                    QApplication.processEvents()
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
            self.alarm()

        elif self.melody==1:
            self.audio()
            self.ui.MplWidget.canvas.axes.axis('off')
            array = self.B
            len_2 = len(self.B)
            t = np.linspace(1, len_2, len_2)
            half_first, half_second = half_array.half_array(array)
            half_first = insertion.insertion_sort(half_first)
            half_second = insertion.insertion_sort(half_second)
            half_first = np.append(half_first, 99999)
            half_second = np.append(half_second, 99999)
            i = 0
            j = 0
            for counter in range(0, len(array)):
                if half_first[i] <= half_second[j]:
                    array[counter] = half_first[i]
                    i = i + 1

                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[i + 1], self.B[i + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
                else:
                    array[counter] = half_second[j]
                    j = j + 1
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(t[counter], self.B[counter], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.bar(t[j + 1], self.B[j + 1], color="red", edgecolor="white")
                    self.ui.MplWidget.canvas.axes.axis('off')
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.draw()
                    self.speed()

                    QApplication.processEvents()
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(t, self.B, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
            mixer.music.stop()
        self.enable()


    def bubble_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()

        n = len(self.B)
        for i in range(0, n - 1):
            for j in range(1, n - i):
                if self.B[j - 1] > self.B[j]:
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j-1], self.B[j-1], color="red",
                                                   edgecolor="black")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red",
                                                   edgecolor="black")
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()

                    self.B[j - 1], self.B[j] = self.B[j], self.B[j - 1]
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j-1], self.B[j-1], color="red",
                                                   edgecolor="black")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red",
                                                   edgecolor="black")
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink",edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                            fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        if self.melody==1:
          mixer.music.stop()
        elif self.melody==2:
            self.alarm()
        self.enable()
    def quick_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        def partition(arr, low, high):

            i = (low - 1)
            pivot = arr[high]

            for j in range(low, high):

                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, arr, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(self.A[i], arr[i], color="red", edgecolor="black")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j], arr[j], color="red", edgecolor="black")
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(np.linspace(1, len(arr), len(arr)), arr, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
            self.speed()
            QApplication.processEvents()
            return (i + 1)

        def quick_sort(arr, low, high):

            if low < high:
                pi = partition(arr, low, high)
                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        low = 0
        high = len(self.B) - 1
        quick_sort(self.B, low, high)
        self.ui.MplWidget.canvas.axes.clear()

        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                            fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        if self.melody==1:
            mixer.music.stop()
        elif self.melody==2:
            self.alarm()
        self.enable()
    def heap_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        def heapify(arr, n, i):
            largest = i  # largest value
            l = 2 * i + 1  # left
            r = 2 * i + 2  # right
            # if left child exists
            if l < n and arr[i] < arr[l]:
                largest = l
            # if right child exits
            if r < n and arr[largest] < arr[r]:
                largest = r
            # root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                # root.
                heapify(arr, n, largest)


        # sort
        def heapSort(arr):
            n = len(arr)
            # maxheap
            for i in range(n, -1, -1):
                heapify(arr, n, i)
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                self.ui.MplWidget.canvas.axes.bar(self.A[i//2], self.B[i//2], color="red",
                                              edgecolor="white")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.4, v + 0.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.speed()
                QApplication.processEvents()
            # element extraction
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # swap
                heapify(arr, i, 0)
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red",
                                                  edgecolor="white")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.4, v + 0.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.speed()
                QApplication.processEvents()
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.4, v + 0.5, " " + str(v), color='purple', va='center', ha='right',
                                                fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
        heapSort(self.B)
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()

    def counting_app(self):
       self.disable()
       self.melody=self.ui.dial_sound.value()
       if self.melody==1:
        self.audio()
       maxvalue=int(max(self.B))
       minvalue=int(min(self.B))
       n=maxvalue-minvalue+1
       C=[]
       D=[]
       for k in range(n):
           a=0
           C.append(a)
       for m in range(len(self.B)):
           b=0
           D.append(b)
       for i in range(0,len(self.B)):
           C[self.B[i]-minvalue] +=1
       for j in range(1,len(C)):
           C[j] += C[j-1]
       for i in range(len(self.B)-1,-1,-1):
           D[C[self.B[i]-minvalue]-1]=self.B[i]
           C[self.B[i]-minvalue] -=1
       for j in range(len(self.B)-1):
           self.ui.MplWidget.canvas.axes.clear()
           self.ui.MplWidget.canvas.axes.bar(self.A,self.B,color="pink",edgecolor="purple")
           self.ui.MplWidget.canvas.axes.bar(self.A[j],self.B[j],color="red",edgecolor="black")

           for k, v in enumerate(self.B):
               self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                  ha='right',
                                                  fontweight='bold', fontsize=8)
           self.ui.MplWidget.canvas.axes.axis('off')
           self.ui.MplWidget.canvas.draw()
           self.speed()
           QApplication.processEvents()
       for i in range(0,len(self.B)):
           self.B[i]=D[i]
           self.ui.MplWidget.canvas.axes.clear()
           self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
           self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red", edgecolor="black")

           for k, v in enumerate(self.B):
               self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                  ha='right',
                                                  fontweight='bold', fontsize=8)
           self.ui.MplWidget.canvas.axes.axis('off')
           self.ui.MplWidget.canvas.draw()
           self.speed()
           QApplication.processEvents()

       self.ui.MplWidget.canvas.axes.clear()
       self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")


       for k, v in enumerate(self.B):
           self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                              fontweight='bold', fontsize=8)
       self.ui.MplWidget.canvas.axes.axis('off')
       self.ui.MplWidget.canvas.draw()
       self.speed()
       QApplication.processEvents()
       if self.melody == 1:
           mixer.music.stop()
       elif self.melody == 2:
           self.alarm()
       self.enable()

    def radix_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        array = self.B
        max_element = max(array)
        place = 1
        while max_element // place > 0:
            size = len(array)
            output = [0] * size
            count = [0] * 10
            for i in range(0, size):
                index = array[i] // place
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            i = size - 1
            while i >= 0:
                index = array[i] // place
                output[count[index % 10] - 1] = array[i]
                count[index % 10] -= 1
                i -= 1
            for i in range(0, size):
                array[i] = output[i]
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, array, color="pink", edgecolor="purple")
                self.ui.MplWidget.canvas.axes.bar(self.A[i], array[i], color="red", edgecolor="black")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.speed()
                QApplication.processEvents()

            place *= 10
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(np.arange(len(self.array)), self.array, color="pink", edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                               fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        self.enable()


    def bucket_app(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        array = self.B
        largest = max(array)
        length = len(array)
        size = largest / length

        buckets = [[] for _ in range(length)]
        for i in range(length):
            j = int(array[i] / size)
            if j != length:
                buckets[j].append(array[i])
            else:
                buckets[length - 1].append(array[i])

        for i in range(length):
            for i in range(1, len(array)):
                temp = array[i]
                j = i - 1
                while (j >= 0 and temp < array[j]):
                    array[j + 1] = array[j]
                    j = j - 1
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, array, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(self.A[i], array[i], color="red", edgecolor="black")
                    self.ui.MplWidget.canvas.axes.bar(self.A[j + 1], array[j + 1], color="red", edgecolor="black")
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
                array[j + 1] = temp

        result = []
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()
        for i in range(length):
            result = result + buckets[i]
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(np.arange(len(self.array)), self.array, color="pink", edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center', ha='right',
                                               fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        self.enable()

    def shell_sort(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        gap = len(self.B) // 2

        while gap > 0:
            i = 0
            j = gap

            while j < len(self.B):

                if self.B[i] > self.B[j]:
                    self.B[i], self.B[j] = self.B[j], self.B[i]

                i += 1
                j += 1

                k = i
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red", edgecolor="black")
                self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.speed()
                QApplication.processEvents()
                while k - gap > -1:

                    if self.B[k - gap] > self.B[k]:
                        self.B[k - gap], self.B[k] = self.B[k], self.B[k - gap]
                        self.ui.MplWidget.canvas.axes.clear()
                        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                        self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red", edgecolor="black")
                        self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                        self.ui.MplWidget.canvas.axes.axis('off')
                        self.ui.MplWidget.canvas.draw()
                        self.speed()
                        QApplication.processEvents()
                    k -= 1
                    self.ui.MplWidget.canvas.axes.clear()
                    self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                    self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red", edgecolor="black")
                    self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
                    self.speed()
                    QApplication.processEvents()
            gap //= 2
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
            self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()
    def combsort(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        gap = len(self.B)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))  # minimum gap is 1
            swaps = False
            for i in range(len(self.B) - gap):
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red", edgecolor="black")
                self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=8)
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
                self.speed()
                QApplication.processEvents()
                j = i + gap
                if self.B[i] > self.B[j]:
                    self.B[i], self.B[j] = self.B[j], self.B[i]
                    swaps = True
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(self.A[i], self.B[i], color="red", edgecolor="black")
        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
        self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                               ha='right',
                                               fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.draw()
        self.enable()
    def gnome(self):
        self.disable()
        self.melody=self.ui.dial_sound.value()
        if self.melody==1:
            self.audio()
        n = len(self.B)
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if self.B[index] >= self.B[index - 1]:
                index = index + 1
            else:
                self.B[index], self.B[index - 1] = self.B[index - 1], self.B[index]
                index = index - 1
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
            self.ui.MplWidget.canvas.axes.bar(self.A[index-1], self.B[index-1], color="red", edgecolor="black")

            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
            self.speed()
            QApplication.processEvents()
        if self.melody == 1:
            mixer.music.stop()
        elif self.melody == 2:
            self.alarm()
        self.enable()
        return self.B


        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
        self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                               ha='right',
                                               fontweight='bold', fontsize=8)
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()
        self.enable()

    def selection(self):
       self.disable()
       self.melody= self.ui.dial_sound.value()
       if self.melody==1:
            self.audio()
       for i in range(len(self.B)):


           min_idx = i
           for j in range(i + 1, len(self.B)):
               if self.B[min_idx] > self.B[j]:
                   min_idx = j
                   self.ui.MplWidget.canvas.axes.clear()
                   self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color='pink',edgecolor="purple")
                   self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red",edgecolor="black")
                   self.ui.MplWidget.canvas.axes.bar(self.A[min_idx], self.B[min_idx], color="red",edgecolor="black")
                   self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
                   self.ui.MplWidget.canvas.axes.axis('off')
                   for k, v in enumerate(self.B):
                       self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                          ha='right',
                                                          fontweight='bold', fontsize=8)
                   self.ui.MplWidget.canvas.draw()
                   self.speed()
                   QApplication.processEvents()


           self.B[i], self.B[min_idx] = self.B[min_idx], self.B[i]
       self.ui.MplWidget.canvas.axes.clear()
       self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color='pink', edgecolor="purple")
       self.ui.MplWidget.canvas.axes.bar(self.A[j], self.B[j], color="red", edgecolor="black")
       self.ui.MplWidget.canvas.axes.bar(self.A[min_idx], self.B[min_idx], color="red", edgecolor="black")
       self.ui.MplWidget.canvas.axes.patch.set_alpha(0)
       self.ui.MplWidget.canvas.axes.axis('off')
       for k, v in enumerate(self.B):
           self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                              ha='right',
                                              fontweight='bold', fontsize=8)
       self.ui.MplWidget.canvas.draw()
       self.speed()
       QApplication.processEvents()
       if self.melody == 1:
           mixer.music.stop()
       elif self.melody == 2:
           self.alarm()
       self.enable()
    def visibility(self):
        v=self.ui.horizontalSlider.value()
        if v==1:
            self.ui.MplWidget.hide()
            self.ui.label_19.show()
        else:
            self.ui.MplWidget.show()
            self.ui.label_19.hide()

    def default(self):
        self.ui.MplWidget.canvas.axes.axis('off')

        self.A = []
        self.B = []
        self.ui.dial_2.setValue(numpy.random.randint(1, 15))
        n=self.ui.dial_2.value()
        self.ui.dial.setValue(numpy.random.randint(1, 5))
        m=self.ui.dial.value()
        self.ui.lcdNumber.display(n)
        self.ui.lcdNumber_2.display(m)
        self.ui.lcdNumber_4.display(n * m)
        self.ui.spinBox.setValue(numpy.random.randint(10,500))
        max_value=self.ui.spinBox.value()
        if self.ui.checkBox_13.isChecked():
            for i in range(n * m):
                r = numpy.random.randint(1, max_value)
                if r not in self.B:
                    self.B.append(r)
            s = 1
            for j in range(len(self.B)):
                self.A.append(s)
                s = s + 1
            self.ui.MplWidget.canvas.axes.clear()  # clear graph

            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink",
                                              edgecolor="purple")  # set the graph for input list
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="purple",
                                                   va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
        else:
            for i in range(n * m):
                value = numpy.random.randint(1, max_value)
                self.B.append(value)
                print("B", self.B)
            s = 1
            for j in range(len(self.B)):
                self.A.append(s)
                s = s + 1
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=10)

            # self.ui.MplWidget.canvas.axes.bar(self.A, self.B)
            # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
            # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
    def your_array(self):

            input = self.ui.lineEdit_4.text()
            self.x= ast.literal_eval(input)
            self.B=[]
            self.A = []
            for i in range(len(self.x)):
                self.A.append(i+1)
            for i in range(len(self.x)):
                self.B.append(self.x[i])

            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="purple",
                                                   va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            # self.ui.MplWidget.canvas.axes.bar(self.A, self.B)
            # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
            # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()


    def update_graph(self):


        self.ui.MplWidget.canvas.axes.axis('off')

        self.A = []
        self.B = []
        n=self.ui.dial_2.value()
        self.ui.lcdNumber.display(n)
        m=self.ui.dial.value()
        self.ui.lcdNumber_2.display(m)
        self.ui.lcdNumber_4.display(n*m)
        max_value=self.ui.spinBox.value()
        self.seed = self.ui.spinBox_2.value()
        self.length=n*m
        if self.ui.checkBox_13.isChecked():
            for i in range(n*m):
                r = numpy.random.randint(1, max_value)
                if r not in self.B:
                    self.B.append(r)
            s = 1
            for j in range(len(self.B)):
                self.A.append(s)
                s = s + 1
            self.ui.MplWidget.canvas.axes.clear()  # clear graph

            self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink",
                                              edgecolor="purple")  # set the graph for input list
            for k, v in enumerate(self.B):
                self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="purple",
                                                   va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget.canvas.axes.axis('off')
            self.ui.MplWidget.canvas.draw()
        else:


            if self.ui.radioButton.isChecked():
                    np.random.seed(self.seed)
                    self.B = np.random.randint(1, 200, n * m)
                    self.x = []  # list for x asis values for graph
                    for i in range(len(self.B)):
                        self.x.append(i + 1)
                    s = 1
                    for j in range(len(self.B)):
                        self.A.append(s)
                        s = s + 1
                    self.ui.MplWidget.canvas.axes.clear()  # clear graph

                    self.ui.MplWidget.canvas.axes.bar(self.x, self.B, color="pink",edgecolor="purple")  # set the graph for input list
                    for k, v in enumerate(self.B):
                        self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="purple",
                                                           va='center',
                                                           ha='right',
                                                           fontweight='bold', fontsize=8)
                    self.ui.MplWidget.canvas.axes.axis('off')
                    self.ui.MplWidget.canvas.draw()
            else:
                for i in range(n * m):
                    value = numpy.random.randint(1, max_value)
                    self.B.append(value)
                    print("B", self.B)
                s = 1
                for j in range(len(self.B)):
                    self.A.append(s)
                    s = s + 1
                self.ui.MplWidget.canvas.axes.clear()
                self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
                for k, v in enumerate(self.B):
                    self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                       ha='right',
                                                       fontweight='bold', fontsize=10)

                # self.ui.MplWidget.canvas.axes.bar(self.A, self.B)
                # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
                # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
                self.ui.MplWidget.canvas.axes.axis('off')
                self.ui.MplWidget.canvas.draw()
    def add_num(self):
        arr=self.ui.lineEdit_5.text()
        arr=ast.literal_eval(arr)
        print(arr)
        self.B.append(arr)
        print(self.B)
        self.length = len(self.B)
        print(self.length)
        s = 1
        self.A=[]
        for j in range(len(self.B)):
            self.A.append(s)
            s = s + 1
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.bar(self.A, self.B, color="pink", edgecolor="purple")
        for k, v in enumerate(self.B):
            self.ui.MplWidget.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                               ha='right',
                                               fontweight='bold', fontsize=10)

        # self.ui.MplWidget.canvas.axes.bar(self.A, self.B)
        # self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        # self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.ui.MplWidget.canvas.axes.axis('off')
        self.ui.MplWidget.canvas.draw()

    def fib_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.fib_index)
        movie=QMovie('f.gif')
        self.ui.label_14.setMovie(movie)
        movie.start()
        self.ui.horizontalSlider_2.valueChanged.connect(self.visibility_fib)
        self.ui.label_14.hide()
        self.ui.pushButton_3.clicked.connect(self.fib)
        self.addToolBar(NavigationToolbar(self.ui.MplWidget_2.canvas, self))
        self.ui.MplWidget_2.canvas.axes.axis('off')
        self.ui.pushButton_5.clicked.connect(self.golden)
    def golden(self):
        self.page = page()
        self.page.show()


    def fib(self):
        def Fibonacci(n):


            if n < 0:
                print("Incorrect input")


            elif n == 1:
                return 0


            elif n == 2 or n == 3:
                return 1

            else:
                return Fibonacci(n - 1) + Fibonacci(n - 2)
        index=int(self.ui.lineEdit.text())
        self.ui.lcdNumber_5.display(Fibonacci(index))
        f=[]
        self.A=[]
        if index<0 :
            QMessageBox.warning(self, "Error", "Please Enter A Valid Number !")
        else:
            for i in range(1,index+1):
                a=Fibonacci(i)
                f.append(a)
            s = 1
            for j in range(len(f)):
                self.A.append(s)
                s = s + 1
            self.ui.MplWidget_2.canvas.axes.clear()
            self.ui.MplWidget_2.canvas.axes.bar(self.A, f, color="salmon", edgecolor="red")
            self.ui.MplWidget_2.canvas.axes.bar(self.A[len(f)-1], f[index-1], color="red", edgecolor="white")
            for k, v in enumerate(f):
                self.ui.MplWidget_2.canvas.axes.text(k + 1.3, v + 0.5, " " + str(v), color='red', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=10)

            self.ui.MplWidget_2.canvas.axes.axis('off')
            self.ui.MplWidget_2.canvas.draw()


    def visibility_fib(self):
        v = self.ui.horizontalSlider_2.value()
        if v == 1:
            self.ui.MplWidget_2.hide()
            self.ui.label_14.show()
        else:
            self.ui.MplWidget_2.show()
            self.ui.label_14.hide()

    def binary_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.binary_index)
        movie = QMovie('binary_search_tree_example.gif')
        self.ui.label_31.setMovie(movie)
        movie.start()
        self.ui.horizontalSlider_3.valueChanged.connect(self.visibility_b)
        self.ui.label_31.hide()
        self.addToolBar(NavigationToolbar(self.ui.MplWidget_3.canvas, self))
        self.ui.MplWidget_3.canvas.axes.axis('off')
        self.ui.pushButton_6.clicked.connect(self.generate_array)
        self.ui.pushButton_7.clicked.connect(self.sort_binary)
        self.ui.pushButton_8.clicked.connect(self.search)
        self.ui.pushButton_19.clicked.connect(self.bin_default)
        self.ui.pushButton_37.clicked.connect(self.savebin)
        self.ui.pushButton_38.clicked.connect(self.getbin)
        self.ui.pushButton_36.clicked.connect(self.clearbin)

    def savebin(self):
        self.txt()
    def getbin(self):
        self.save()
    def clearbin(self):
        self.ui.MplWidget_3.canvas.axes.clear()
        self.ui.MplWidget_3.canvas.axes.patch.set_alpha(0)
        self.ui.MplWidget_3.canvas.axes.axis("off")
        self.ui.MplWidget_3.canvas.draw()
    def visibility_b(self):
        v=self.ui.horizontalSlider_3.value()
        if v==1:
            self.ui.MplWidget_3.hide()
            self.ui.label_31.show()
        else:
            self.ui.MplWidget_3.show()
            self.ui.label_31.hide()

    def bin_default(self):
        self.ui.MplWidget.canvas.axes.axis('off')
        self.bin_x = []
        self.array_binary = []
        self.ui.dial_3.setValue(numpy.random.randint(1,15))
        n = self.ui.dial_3.value()
        self.ui.lcdNumber_6.display(n)
        self.ui.dial_4.setValue(numpy.random.randint(1,5))
        m = self.ui.dial_4.value()
        self.ui.lcdNumber_7.display(m)
        self.ui.lcdNumber_8.display(n * m)
        self.ui.spinBox_3.setValue(numpy.random.randint(10,500))
        max_value = self.ui.spinBox_3.value()
        for i in range(n * m):
            value = numpy.random.randint(1, max_value)
            self.array_binary.append(value)

        s = 1
        for j in range(len(self.array_binary)):
            self.bin_x.append(s)
            s = s + 1
        self.ui.MplWidget_3.canvas.axes.clear()
        self.ui.MplWidget_3.canvas.axes.bar(self.bin_x, self.array_binary, color="mediumpurple", edgecolor="purple")
        for k, v in enumerate(self.array_binary):
            self.ui.MplWidget_3.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget_3.canvas.axes.axis('off')
        self.ui.MplWidget_3.canvas.draw()

    def generate_array(self):
        self.ui.MplWidget.canvas.axes.axis('off')

        self.bin_x = []
        self.array_binary = []
        n = self.ui.dial_3.value()
        self.ui.lcdNumber_6.display(n)
        m = self.ui.dial_4.value()
        self.ui.lcdNumber_7.display(m)
        self.ui.lcdNumber_8.display(n * m)
        max_value = self.ui.spinBox_3.value()
        self.seed_bin = self.ui.spinBox_4.value()

        if self.ui.radioButton_2.isChecked():
            np.random.seed(self.seed_bin)
            self.array_binary = np.random.randint(1, max_value, n * m)
            self.x2 = []  # list for x asis values for graph
            for i in range(len(self.array_binary)):
                self.x2.append(i + 1)
            s = 1
            for j in range(len(self.array_binary)):
                self.bin_x.append(s)
                s = s + 1
            self.ui.MplWidget_3.canvas.axes.clear()  # clear graph

            self.ui.MplWidget_3.canvas.axes.bar(self.x2, self.array_binary, color="mediumpurple",
                                              edgecolor="purple")  # set the graph for input list
            for k, v in enumerate(self.array_binary):
                self.ui.MplWidget_3.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="purple",
                                                   va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=8)
            self.ui.MplWidget_3.canvas.axes.axis('off')
            self.ui.MplWidget_3.canvas.draw()
        else:
            for i in range(n * m):
                value = numpy.random.randint(1, max_value)
                self.array_binary.append(value)

            s = 1
            for j in range(len(self.array_binary)):
                self.bin_x.append(s)
                s = s + 1
            self.ui.MplWidget_3.canvas.axes.clear()
            self.ui.MplWidget_3.canvas.axes.bar(self.bin_x, self.array_binary, color="mediumpurple", edgecolor="purple")
            for k, v in enumerate(self.array_binary):
                self.ui.MplWidget_3.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                   ha='right',
                                                   fontweight='bold', fontsize=10)

            self.ui.MplWidget_3.canvas.axes.axis('off')
            self.ui.MplWidget_3.canvas.draw()

    def sort_binary(self):
        insertionSort(self.array_binary)
        self.ui.MplWidget_3.canvas.axes.clear()
        self.ui.MplWidget_3.canvas.axes.bar(self.bin_x, self.array_binary, color="mediumpurple", edgecolor="purple")
        for k, v in enumerate(self.array_binary):
            self.ui.MplWidget_3.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget_3.canvas.axes.axis('off')
        self.ui.MplWidget_3.canvas.draw()
        self.ui.pushButton_8.setEnabled(True)

    def search(self):
        num=int(self.ui.lineEdit_2.text())



        def linearSearch(array, n, x):


            for i in range(0, n):
                if (array[i] == x):
                    return i
            return -1
        a=linearSearch(self.array_binary,len(self.array_binary),num)
        if  a==-1:
            QMessageBox.warning(self, "Error", "Please Enter A Valid Number !")

        else:
                index=binarysearch(self.array_binary,num,0,len(self.array_binary))
                self.ui.lcdNumber_9.display(index)
                self.ui.MplWidget_3.canvas.axes.clear()
                self.ui.MplWidget_3.canvas.axes.bar(self.bin_x, self.array_binary, color="mediumpurple", edgecolor="purple")
                self.ui.MplWidget_3.canvas.axes.bar(self.bin_x[index],self.array_binary[index],color="pink",edgecolor="white")
                for k, v in enumerate(self.array_binary):
                    self.ui.MplWidget_3.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='purple', va='center',
                                                         ha='right',
                                                         fontweight='bold', fontsize=10)

                self.ui.MplWidget_3.canvas.axes.axis('off')
                self.ui.MplWidget_3.canvas.draw()







    def ith_smallest(self):
        self.ui.stackedWidget.setCurrentIndex(self.ith_index)
        movie = QMovie('numgif.gif')
        self.ui.label_41.setMovie(movie)
        movie.start()
        self.ui.horizontalSlider_4.valueChanged.connect(self.visibility_i)
        self.ui.label_41.hide()
        self.addToolBar(NavigationToolbar(self.ui.MplWidget_4.canvas, self))
        self.ui.MplWidget_4.canvas.axes.axis('off')
        self.ui.pushButton_9.clicked.connect(self.array_gen)
        self.ui.pushButton_10.clicked.connect(self.sort_i)
        self.ui.pushButton_11.clicked.connect(self.find_smallest)
        self.ui.pushButton_20.clicked.connect(self.i_default)
        self.ui.pushButton_39.clicked.connect(self.save_i)
        self.ui.pushButton_40.clicked.connect(self.get)
        self.ui.pushButton_41.clicked.connect(self.clean_i)

    def save_i(self):
        self.txt()
    def get(self):
        self.save()
    def clean_i(self):
        self.ui.MplWidget_4.canvas.axes.clear()
        self.ui.MplWidget_4.canvas.axes.patch.set_alpha(0)
        self.ui.MplWidget_4.canvas.axes.axis("off")
        self.ui.MplWidget_4.canvas.draw()
    def visibility_i(self):
        v = self.ui.horizontalSlider_4.value()
        if v == 1:
            self.ui.MplWidget_4.hide()
            self.ui.label_41.show()
        else:
            self.ui.MplWidget_4.show()
            self.ui.label_41.hide()
    def i_default(self):
        self.ui.MplWidget_4.canvas.axes.axis('off')

        self.ith_x = []
        self.array_ith = []
        self.ui.dial_5.setValue(numpy.random.randint(1,15))
        n = self.ui.dial_5.value()
        self.ui.lcdNumber_10.display(n)
        self.ui.dial_6.setValue(numpy.random.randint(1,5))
        m = self.ui.dial_6.value()
        self.ui.lcdNumber_11.display(m)
        self.ui.lcdNumber_12.display(n * m)
        self.ui.spinBox_5.setValue(numpy.random.randint(10,500))
        max_value = self.ui.spinBox_5.value()
        for i in range(n * m):
            value = numpy.random.randint(1, max_value)
            self.array_ith.append(value)

        s = 1
        for j in range(len(self.array_ith)):
            self.ith_x.append(s)
            s = s + 1
        self.ui.MplWidget_4.canvas.axes.clear()
        self.ui.MplWidget_4.canvas.axes.bar(self.ith_x, self.array_ith, color="deepskyblue", edgecolor="aqua")
        for k, v in enumerate(self.array_ith):
            self.ui.MplWidget_4.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='aqua', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget_4.canvas.axes.axis('off')
        self.ui.MplWidget_4.canvas.draw()


    def array_gen(self):
        self.ui.MplWidget_4.canvas.axes.axis('off')

        self.ith_x = []
        self.array_ith = []
        n = self.ui.dial_5.value()
        self.ui.lcdNumber_10.display(n)
        m = self.ui.dial_6.value()
        self.ui.lcdNumber_11.display(m)
        self.ui.lcdNumber_12.display(n * m)
        max_value = self.ui.spinBox_5.value()
        self.seed_ith = self.ui.spinBox_6.value()

        if self.ui.radioButton_3.isChecked():
            np.random.seed(self.seed_ith)
            self.array_ith = np.random.randint(1, max_value, n * m)
            self.x3 = []  # list for x asis values for graph
            for i in range(len(self.array_ith)):
                self.x3.append(i + 1)
            s = 1
            for j in range(len(self.array_ith)):
                self.ith_x.append(s)
                s = s + 1
            self.ui.MplWidget_4.canvas.axes.clear()  # clear graph

            self.ui.MplWidget_4.canvas.axes.bar(self.x3, self.array_ith, color="deepskyblue",
                                                edgecolor="aqua")  # set the graph for input list
            for k, v in enumerate(self.array_ith):
                self.ui.MplWidget_4.canvas.axes.text(k + 1.3, v + 2.50, " " + str(v), color="aqua",
                                                     va='center',
                                                     ha='right',
                                                     fontweight='bold', fontsize=8)
            self.ui.MplWidget_4.canvas.axes.axis('off')
            self.ui.MplWidget_4.canvas.draw()
        else:
            for i in range(n * m):
                value = numpy.random.randint(1, max_value)
                self.array_ith.append(value)

            s = 1
            for j in range(len(self.array_ith)):
                self.ith_x.append(s)
                s = s + 1
            self.ui.MplWidget_4.canvas.axes.clear()
            self.ui.MplWidget_4.canvas.axes.bar(self.ith_x, self.array_ith, color="deepskyblue", edgecolor="aqua")
            for k, v in enumerate(self.array_ith):
                self.ui.MplWidget_4.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='aqua', va='center',
                                                     ha='right',
                                                     fontweight='bold', fontsize=10)

            self.ui.MplWidget_4.canvas.axes.axis('off')
            self.ui.MplWidget_4.canvas.draw()

    def sort_i(self):
        insertionSort(self.array_ith)
        self.ui.MplWidget_4.canvas.axes.clear()
        self.ui.MplWidget_4.canvas.axes.bar(self.ith_x, self.array_ith, color="deepskyblue", edgecolor="aqua")
        for k, v in enumerate(self.array_ith):
            self.ui.MplWidget_4.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='aqua', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget_4.canvas.axes.axis('off')
        self.ui.MplWidget_4.canvas.draw()
        self.ui.pushButton_11.setEnabled(True)
    def find_smallest(self):
        index=int(self.ui.lineEdit_3.text())
        if index<=0 or index>len(self.array_ith):
            QMessageBox.warning(self, "Error", "Please Enter A Valid Number !")

        a=rand_select(self.array_ith,0,len(self.array_ith)-1,index)
        self.ui.lcdNumber_13.display(a)
        self.ui.MplWidget_4.canvas.axes.clear()
        self.ui.MplWidget_4.canvas.axes.bar(self.ith_x, self.array_ith, color="deepskyblue", edgecolor="aqua")
        self.ui.MplWidget_4.canvas.axes.bar(self.ith_x[index-1], self.array_ith[index-1], color="aqua", edgecolor="white")
        for k, v in enumerate(self.array_ith):
            self.ui.MplWidget_4.canvas.axes.text(k + 1.3, v + 2.5, " " + str(v), color='aqua', va='center',
                                                 ha='right',
                                                 fontweight='bold', fontsize=10)

        self.ui.MplWidget_4.canvas.axes.axis('off')
        self.ui.MplWidget_4.canvas.draw()


    def random_matrix(self):
        self.ui.stackedWidget.setCurrentIndex(self.matrix_mult)
        self.ui.pushButton_12.clicked.connect(self.matrix)
        self.ui.pushButton_15.clicked.connect(self.mult)
        self.ui.pushButton_13.clicked.connect(self.sum)
        self.ui.pushButton_14.clicked.connect(self.sub)
        self.ui.horizontalSlider_5.valueChanged.connect(self.visibility_m)
        self.ui.pushButton_46.clicked.connect(self.cl)
        self.ui.pushButton_45.clicked.connect(self.matrix_save)
        self.ui.label_42.show()
        self.ui.tableWidget.hide()
        self.ui.tableWidget_2.hide()
        self.ui.tableWidget_3.hide()
        movie = QMovie('m.gif')
        self.ui.label_42.setMovie(movie)
        movie.start()
    def matrix_save(self):
        root=tk.Tk()
        root.withdraw()
        filepath = filedialog.asksaveasfilename(defaultextension="csv",filetypes=[("csv file", "*.csv"), ("All Files", "*.*")],)
        with open(filepath, "w") as output_file:
            row = 0
            for i in range(len(self.result_matrix)):
                column = 0
                for j in range(len(self.result_matrix[0])):
                    text=(row, column, self.result_matrix[i][j])
                    column += 1
                row += 1
            text = text.strip("[")
            text = text.strip("]")
            output_file.write(text)

    def cl(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_3.clear()
    def visibility_m(self):
        v = self.ui.horizontalSlider_5.value()
        if v == 1:
            self.ui.tableWidget.hide()
            self.ui.tableWidget_2.hide()
            self.ui.tableWidget_3.hide()
            self.ui.label_42.show()
        else:
            self.ui.tableWidget.show()
            self.ui.tableWidget_2.show()
            self.ui.tableWidget_3.show()
            self.ui.label_42.hide()

    def sub(self):

            result_matrix = [[0 for x in range(len(self.matrix_2[0]))] for y in
                             range(len(self.matrix_1))]
            for i in range(len(self.matrix_1)):
                for j in range(len(self.matrix_1[0])):
                    result_matrix[i][j] = self.matrix_1[i][j] - self.matrix_2[i][j]
            self.ui.tableWidget_3.setRowCount(self.row_2)
            self.ui.tableWidget_3.setColumnCount(self.column_1)
            for i in range(self.row_2):
                self.ui.tableWidget_3.setRowHeight(i, 250 / self.row_2)
            for i in range(self.column_1):
                self.ui.tableWidget_3.setColumnWidth(i, 250 / self.column_1)
            for i in range(self.row_2):
                for j in range(self.column_1):
                    cell = QTableWidgetItem(str(result_matrix[i][j]))
                    self.ui.tableWidget_3.setItem(i, j, cell)

    def sum(self):

        result_matrix = [[0 for x in range(len(self.matrix_2[0]))] for y in
                         range(len(self.matrix_1))]
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_1[0])):
                result_matrix[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        self.ui.tableWidget_3.setRowCount(self.row_2)
        self.ui.tableWidget_3.setColumnCount(self.column_1)
        for i in range(self.row_2):
            self.ui.tableWidget_3.setRowHeight(i, 250 / self.row_2)
        for i in range(self.column_1):
            self.ui.tableWidget_3.setColumnWidth(i, 250 / self.column_1)
        for i in range(self.row_2):
            for j in range(self.column_1):
                cell = QTableWidgetItem(str(result_matrix[i][j]))  # ADD NUMBERS TO TEMPORARY VALUE
                self.ui.tableWidget_3.setItem(i, j, cell)  # ADD TEMPORARY VALUE TO CELL


    def mult(self):

                    self.result_matrix = [[0 for x in range(len(self.matrix_2[0]))] for y in
                                          range(len(self.matrix_1))]
                    for i in range(len(self.matrix_1)):
                        for j in range(len(self.matrix_2[0])):
                            for k in range(len(self.matrix_2)):
                                self.result_matrix[i][j] += self.matrix_1[i][k] * self.matrix_2[k][j]
                    self.ui.tableWidget_3.setRowCount(self.row_2)
                    self.ui.tableWidget_3.setColumnCount(self.column_1)
                    for i in range(self.row_2):
                        self.ui.tableWidget_3.setRowHeight(i, 250 / self.row_2)
                    for i in range(self.column_1):
                        self.ui.tableWidget_3.setColumnWidth(i, 250 / self.column_1)
                    for i in range(self.row_2):
                        for j in range(self.column_1):
                            cell = QTableWidgetItem(str(self.result_matrix[i][j]))
                            self.ui.tableWidget_3.setItem(i, j, cell)

    def matrix(self):
        self.row_1 = self.ui.spinBox_7.value()
        self.column_1 = self.ui.spinBox_8.value()
        self.row_2 = self.ui.spinBox_9.value()
        self.column_2 = self.ui.spinBox_10.value()

        self.ui.tableWidget.setRowCount(self.row_1)
        self.ui.tableWidget.setColumnCount(self.column_1)
        self.ui.tableWidget_2.setRowCount(self.row_2)
        self.ui.tableWidget_2.setColumnCount(self.column_2)
        for i in range(self.column_1):
            self.ui.tableWidget.setColumnWidth(i, 250 / self.column_1)
        for i in range(self.row_1):
            self.ui.tableWidget.setRowHeight(i, 250 / self.row_1)
        for i in range(self.column_2):
            self.ui.tableWidget_2.setColumnWidth(i, 250 / self.column_2)
        for i in range(self.row_2):
            self.ui.tableWidget_2.setRowHeight(i, 250 / self.row_2)
        self.matrix_1 = []
        self.matrix_2 = []

        for i in range(self.row_2):
            B = []
            for j in range(self.column_2):
                value = rd.randint(0, 100)
                B.append(value)
            self.matrix_2.append(B)

        for i in range(self.row_2):
            for j in range(self.column_2):
                cell = QTableWidgetItem(str(self.matrix_2[i][j]))
                self.ui.tableWidget_2.setItem(i, j, cell)

        for i in range(self.row_1):
            C = []
            for j in range(self.column_1):
                value = rd.randint(0, 100)
                C.append(value)
            self.matrix_1.append(C)

        for i in range(self.row_1):
            for j in range(self.column_1):
                cell = QTableWidgetItem(str(self.matrix_1[i][j]))
                self.ui.tableWidget.setItem(i, j, cell)

        if (self.row_1!=self.row_2) or (self.column_1!=self.column_2):
            self.ui.pushButton_13.setEnabled(False)
            self.ui.pushButton_14.setEnabled(False)
        else:
            self.ui.pushButton_13.setEnabled(True)
            self.ui.pushButton_14.setEnabled(True)
        if self.column_1!=self.row_2:
            self.ui.pushButton_15.setEnabled(False)
        else:
            self.ui.pushButton_15.setEnabled(True)


    def comparison(self):
        self.ui.stackedWidget.setCurrentIndex(self.comp_index)
        self.ui.pushButton_16.clicked.connect(self.compare)
        self.ui.pushButton_17.clicked.connect(self.compare_all)
        self.ui.pushButton_34.clicked.connect(self.reset)
        movie = QMovie('c.gif')
        self.ui.label_71.setMovie(movie)
        movie.start()
        self.ui.label_71.hide()
        self.ui.horizontalSlider_6.valueChanged.connect(self.vis)
        self.ui.pushButton_35.clicked.connect(self.scatter)
        self.ui.pushButton_42.clicked.connect(self.scatter_all)

    def reset(self):
        self.ui.MplWidget_5.canvas.axes.clear()
        self.ui.MplWidget_5.canvas.draw()

    def compare(self):


        if self.ui.checkBox.isChecked():
            elements = list()
            times = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, (100* i), 100 * i)
                # print(i)
                start = time.clock()
                insertionSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements.append(len(a))
                times.append(end - start)

           # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            #self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.plot(elements, times, label='Insertion Sort',color="lime",marker=".")

            self.ui.MplWidget_5.canvas.draw()

        if self.ui.checkBox_3.isChecked():
            elements1 = list()
            times1 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0,100 * i, 100 * i)
                # print(i)
                start = time.clock()
                bubble_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements1.append(len(a))
                times1.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.plot(elements1, times1, label='Bubble Sort', color="cyan", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_5.isChecked():
            elements2 = list()
            times2 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                heapsort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements2.append(len(a))
                times2.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.plot(elements2, times2, label='Heap Sort', color="green", marker=".")

            self.ui.MplWidget_5.canvas.draw()

        if self.ui.checkBox_8.isChecked():
            elements8 = list()
            times8 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                bucket_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements8.append(len(a))
                times8.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.plot(elements8, times8, label='Bucket Sort', color="violet", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_2.isChecked():
            elementsm = list()
            timesm = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                Merge_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsm.append(len(a))
                timesm.append(end - start)


            self.ui.MplWidget_5.canvas.axes.plot(elementsm, timesm, label='Merge Sort', color="gold", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_4.isChecked():
            elementsq = list()
            timesq = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                quicksort(a,0,len(a)-1)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsq.append(len(a))
                timesq.append(end - start)


            self.ui.MplWidget_5.canvas.axes.plot(elementsq, timesq, label='Quick Sort', color="orange", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_6.isChecked():
            elementsc = list()
            timesc = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                count_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsc.append(len(a))
                timesc.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementsc, timesc, label='Counting Sort', color="hotpink", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_7.isChecked():
            elementsr = list()
            timesr = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                radixSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsr.append(len(a))
                timesr.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementsr, timesr, label='Counting Sort', color="firebrick", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_9.isChecked():
            elementsh = list()
            timesh = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                shellSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsh.append(len(a))
                timesh.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementsh, timesh, label='Shell Sort', color="turquoise",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_10.isChecked():
            elementc = list()
            timesc = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                combsort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementc.append(len(a))
                timesc.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementc, timesc, label='Comb Sort', color="yellow",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_11.isChecked():
            elementg = list()
            timeg = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                gnomeSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementg.append(len(a))
                timeg.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementg, timeg, label='Gnome Sort', color="tan",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_12.isChecked():
            elementse = list()
            timese = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                selectionSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementse.append(len(a))
                timese.append(end - start)

            self.ui.MplWidget_5.canvas.axes.plot(elementse, timese, label='Selection Sort', color="magenta",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
    def compare_all(self):
        elements = list()
        times = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, (100 * i), 100 * i)
            # print(i)
            start = time.clock()
            insertionSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements.append(len(a))
            times.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.plot(elements, times, label='Insertion Sort', color="lime", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elements1 = list()
        times1 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            bubble_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements1.append(len(a))
            times1.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.plot(elements1, times1, label='Bubble Sort', color="cyan", marker=".")

        self.ui.MplWidget_5.canvas.draw()


        elements2 = list()
        times2 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            heapsort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements2.append(len(a))
            times2.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.plot(elements2, times2, label='Heap Sort', color="green", marker=".")

        self.ui.MplWidget_5.canvas.draw()


        elements8 = list()
        times8 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            bucket_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements8.append(len(a))
            times8.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.plot(elements8, times8, label='Bucket Sort', color="violet", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsm = list()
        timesm = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            Merge_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsm.append(len(a))
            timesm.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementsm, timesm, label='Merge Sort', color="gold", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsq = list()
        timesq = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            quicksort(a, 0, len(a) - 1)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsq.append(len(a))
            timesq.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementsq, timesq, label='Quick Sort', color="orange", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsc = list()
        timesc = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            count_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsc.append(len(a))
            timesc.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementsc, timesc, label='Counting Sort', color="hotpink", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsr = list()
        timesr = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            radixSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsr.append(len(a))
            timesr.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementsr, timesr, label='Counting Sort', color="firebrick", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsh = list()
        timesh = list()
        for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                shellSort(a)
                end = time.clock()

                        # print("Sorted list is ", a)

                elementsh.append(len(a))
                timesh.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementsh, timesh, label='Shell Sort', color="turquoise",
                                                 marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementc = list()
        timesc = list()
        for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                combsort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementc.append(len(a))
                timesc.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementc, timesc, label='Comb Sort', color="yellow",
                                                 marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementg = list()
        timeg = list()
        for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                gnomeSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementg.append(len(a))
                timeg.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementg, timeg, label='Gnome Sort', color="tan",
                                                 marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementse = list()
        timese = list()
        for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                selectionSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementse.append(len(a))
                timese.append(end - start)

        self.ui.MplWidget_5.canvas.axes.plot(elementse, timese, label='Selection Sort', color="magenta",
                                                 marker=".")
        self.ui.MplWidget_5.canvas.draw()

    def scatter(self):

        if self.ui.checkBox.isChecked():
            elements = list()
            times = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, (100 * i), 100 * i)
                # print(i)
                start = time.clock()
                insertionSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements.append(len(a))
                times.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.scatter(elements, times, label='Insertion Sort', color="lime", marker=".")

            self.ui.MplWidget_5.canvas.draw()

        if self.ui.checkBox_3.isChecked():
            elements1 = list()
            times1 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                bubble_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements1.append(len(a))
                times1.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.scatter(elements1, times1, label='Bubble Sort', color="cyan", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_5.isChecked():
            elements2 = list()
            times2 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                heapsort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements2.append(len(a))
                times2.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.scatter(elements2, times2, label='Heap Sort', color="green", marker=".")

            self.ui.MplWidget_5.canvas.draw()

        if self.ui.checkBox_8.isChecked():
            elements8 = list()
            times8 = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                bucket_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elements8.append(len(a))
                times8.append(end - start)

            # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
            # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
            self.ui.MplWidget_5.canvas.axes.scatter(elements8, times8, label='Bucket Sort', color="violet", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_2.isChecked():
            elementsm = list()
            timesm = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                Merge_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsm.append(len(a))
                timesm.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementsm, timesm, label='Merge Sort', color="gold", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_4.isChecked():
            elementsq = list()
            timesq = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                quicksort(a, 0, len(a) - 1)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsq.append(len(a))
                timesq.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementsq, timesq, label='Quick Sort', color="orange", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_6.isChecked():
            elementsc = list()
            timesc = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                count_sort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsc.append(len(a))
                timesc.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementsc, timesc, label='Counting Sort', color="hotpink", marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_7.isChecked():
            elementsr = list()
            timesr = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                radixSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsr.append(len(a))
                timesr.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementsr, timesr, label='Counting Sort', color="firebrick",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_9.isChecked():
            elementsh = list()
            timesh = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                shellSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementsh.append(len(a))
                timesh.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementsh, timesh, label='Shell Sort', color="turquoise",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_10.isChecked():
            elementc = list()
            timesc = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                combsort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementc.append(len(a))
                timesc.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementc, timesc, label='Comb Sort', color="yellow",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_11.isChecked():
            elementg = list()
            timeg = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                gnomeSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementg.append(len(a))
                timeg.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementg, timeg, label='Gnome Sort', color="tan",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()
        if self.ui.checkBox_12.isChecked():
            elementse = list()
            timese = list()
            for i in range(1, 10):
                # generate some integers
                a = np.random.randint(0, 100 * i, 100 * i)
                # print(i)
                start = time.clock()
                selectionSort(a)
                end = time.clock()

                # print("Sorted list is ", a)

                elementse.append(len(a))
                timese.append(end - start)

            self.ui.MplWidget_5.canvas.axes.scatter(elementse, timese, label='Selection Sort', color="magenta",
                                                 marker=".")

            self.ui.MplWidget_5.canvas.draw()

    def scatter_all(self):
        elements = list()
        times = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, (100 * i), 100 * i)
            # print(i)
            start = time.clock()
            insertionSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements.append(len(a))
            times.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.scatter(elements, times, label='Insertion Sort', color="lime", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elements1 = list()
        times1 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            bubble_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements1.append(len(a))
            times1.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.scatter(elements1, times1, label='Bubble Sort', color="cyan", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elements2 = list()
        times2 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            heapsort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements2.append(len(a))
            times2.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.scatter(elements2, times2, label='Heap Sort', color="green", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elements8 = list()
        times8 = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            bucket_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elements8.append(len(a))
            times8.append(end - start)

        # self.ui.Mplwidget_5.canvas.axes.plt.xlabel('List Length')
        # self.ui.Mplwidget_5.canvas.axes.plt.ylabel('Time Complexity')
        self.ui.MplWidget_5.canvas.axes.scatter(elements8, times8, label='Bucket Sort', color="violet", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsm = list()
        timesm = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            Merge_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsm.append(len(a))
            timesm.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementsm, timesm, label='Merge Sort', color="gold", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsq = list()
        timesq = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            quicksort(a, 0, len(a) - 1)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsq.append(len(a))
            timesq.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementsq, timesq, label='Quick Sort', color="orange", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsc = list()
        timesc = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            count_sort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsc.append(len(a))
            timesc.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementsc, timesc, label='Counting Sort', color="hotpink", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsr = list()
        timesr = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            radixSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsr.append(len(a))
            timesr.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementsr, timesr, label='Counting Sort', color="firebrick", marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementsh = list()
        timesh = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            shellSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementsh.append(len(a))
            timesh.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementsh, timesh, label='Shell Sort', color="turquoise",
                                             marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementc = list()
        timesc = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            combsort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementc.append(len(a))
            timesc.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementc, timesc, label='Comb Sort', color="yellow",
                                             marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementg = list()
        timeg = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            gnomeSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementg.append(len(a))
            timeg.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementg, timeg, label='Gnome Sort', color="tan",
                                             marker=".")

        self.ui.MplWidget_5.canvas.draw()

        elementse = list()
        timese = list()
        for i in range(1, 10):
            # generate some integers
            a = np.random.randint(0, 100 * i, 100 * i)
            # print(i)
            start = time.clock()
            selectionSort(a)
            end = time.clock()

            # print("Sorted list is ", a)

            elementse.append(len(a))
            timese.append(end - start)

        self.ui.MplWidget_5.canvas.axes.scatter(elementse, timese, label='Selection Sort', color="magenta",
                                             marker=".")
        self.ui.MplWidget_5.canvas.draw()

    def vis(self):
        v=self.ui.horizontalSlider_6.value()
        if v==1:
            self.ui.MplWidget_5.hide()
            self.ui.label_71.show()
        else:
            self.ui.MplWidget_5.show()
            self.ui.label_71.hide()
    def exit(self):
        self.ui.stackedWidget.setCurrentIndex(self.exit_index)
        self.ui.pushButton_47.clicked.connect(self.ext)
    def ext(self):
        self.close()

app=QApplication([])
window=homework()
window.show()
app.exec_()