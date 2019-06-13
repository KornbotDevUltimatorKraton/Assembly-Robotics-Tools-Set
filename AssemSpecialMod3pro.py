# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AssemSpecialMod3pro.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout,QLCDNumber,QTextEdit

import sys 
import math  # Math function for the Angle and positioning calculation on the 3d space function 
import itertools # Iter tools looping the Process under the intternal run  
import pyfirmata # Serial hardware communication library 
import time 
import pandas # Data management on the .csv file 
import matplotlib
import microgear.client as microgear # IoT application 
import logging  #log info 
  # Google drive for the cloud command sender application
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive 
AnalogReadA1 = 0 
errorElbow = 0 
Angleelbow = 0 
BaseMesgI = " "
Partbringer = " "

list = [u"Drills", u"Gripper", u"Vacuum", u"Fluidic", u"Laser",u"Soldering iron", u"Cemera image processing"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1412, 880)
        MainWindow.setStyleSheet("color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(70, 260, 50, 64))
        self.dial.setObjectName("dial")
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(140, 260, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(220, 260, 50, 64))
        self.dial_3.setObjectName("dial_3")
        self.dial_4 = QtWidgets.QDial(self.centralwidget)
        self.dial_4.setGeometry(QtCore.QRect(70, 330, 50, 64))
        self.dial_4.setObjectName("dial_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 430, 341, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(150, 490, 331, 16))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 230, 41, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 230, 51, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 320, 111, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 410, 181, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 460, 121, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 10, 131, 17))
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 640, 101, 21))
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 670, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 700, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(26, 730, 111, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 640, 67, 17))
        self.label_11.setObjectName("label_11")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 670, 101, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 700, 101, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 730, 101, 21))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(150, 760, 101, 21))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(150, 790, 101, 21))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 760, 111, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 790, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 610, 211, 17))
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 110, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 150, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 70, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(190, 110, 341, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(190, 150, 341, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(660, 10, 181, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1050, 10, 171, 17))
        self.label_16.setObjectName("label_16")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(640, 600, 591, 201))
        self.textEdit_7.setStyleSheet("color: rgb(136, 138, 133);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(640, 570, 141, 20))
        self.label_17.setObjectName("label_17")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(620, 50, 311, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 91, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 91, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 140, 91, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 170, 121, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 200, 201, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_15.setGeometry(QtCore.QRect(10, 230, 111, 23))
        self.checkBox_15.setObjectName("checkBox_15")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.dial_5 = QtWidgets.QDial(self.centralwidget)
        self.dial_5.setGeometry(QtCore.QRect(320, 260, 50, 64))
        self.dial_5.setObjectName("dial_5")
        self.dial_6 = QtWidgets.QDial(self.centralwidget)
        self.dial_6.setGeometry(QtCore.QRect(390, 260, 50, 64))
        self.dial_6.setObjectName("dial_6")
        self.dial_7 = QtWidgets.QDial(self.centralwidget)
        self.dial_7.setGeometry(QtCore.QRect(460, 260, 50, 64))
        self.dial_7.setObjectName("dial_7")
        self.dial_8 = QtWidgets.QDial(self.centralwidget)
        self.dial_8.setGeometry(QtCore.QRect(330, 340, 50, 64))
        self.dial_8.setObjectName("dial_8")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 230, 41, 17))
        self.label_18.setObjectName("label_18")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(390, 230, 67, 17))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(60, 200, 67, 17))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(470, 230, 51, 17))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(340, 330, 111, 17))
        self.label_22.setObjectName("label_22")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(150, 550, 341, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(150, 530, 181, 17))
        self.label_23.setObjectName("label_23")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(150, 590, 331, 16))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(150, 570, 121, 17))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(20, 530, 121, 20))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(30, 430, 67, 17))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(300, 670, 67, 17))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(300, 700, 67, 17))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(270, 760, 111, 20))
        self.label_29.setObjectName("label_29")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(400, 640, 101, 21))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(400, 760, 101, 21))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(300, 640, 67, 17))
        self.label_30.setObjectName("label_30")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(400, 700, 101, 21))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(400, 730, 101, 21))
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(320, 610, 261, 17))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(270, 790, 121, 20))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(276, 730, 111, 20))
        self.label_33.setObjectName("label_33")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(400, 670, 101, 21))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_13.setGeometry(QtCore.QRect(400, 790, 101, 21))
        self.textEdit_13.setObjectName("textEdit_13")
        self.dial_9 = QtWidgets.QDial(self.centralwidget)
        self.dial_9.setGeometry(QtCore.QRect(530, 510, 50, 64))
        self.dial_9.setObjectName("dial_9")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(510, 490, 91, 17))
        self.label_34.setObjectName("label_34")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 570, 64, 23))
        self.lcdNumber.setStyleSheet("font: 11pt \"Ubuntu\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.lcdNumber.setObjectName("lcdNumber")
        self.dial_10 = QtWidgets.QDial(self.centralwidget)
        self.dial_10.setGeometry(QtCore.QRect(500, 350, 50, 64))
        self.dial_10.setObjectName("dial_10")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(470, 330, 121, 17))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(330, 190, 101, 17))
        self.label_36.setObjectName("label_36")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(980, 50, 461, 261))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 459, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 20, 91, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 80, 91, 23))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 110, 91, 23))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_12.setGeometry(QtCore.QRect(10, 140, 91, 23))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_13.setGeometry(QtCore.QRect(10, 170, 121, 23))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_14.setGeometry(QtCore.QRect(10, 200, 201, 23))
        self.checkBox_14.setObjectName("checkBox_14")
        self.textEdit_14 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_14.setGeometry(QtCore.QRect(110, 20, 181, 21))
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_15.setGeometry(QtCore.QRect(110, 50, 181, 21))
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_16.setGeometry(QtCore.QRect(110, 80, 181, 21))
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_17.setGeometry(QtCore.QRect(110, 110, 181, 21))
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_18.setGeometry(QtCore.QRect(110, 140, 181, 21))
        self.textEdit_18.setObjectName("textEdit_18")
        self.textEdit_19 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_19.setGeometry(QtCore.QRect(140, 170, 181, 21))
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_26 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_26.setGeometry(QtCore.QRect(210, 200, 181, 21))
        self.textEdit_26.setObjectName("textEdit_26")
        self.checkBox_23 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_23.setGeometry(QtCore.QRect(10, 230, 201, 23))
        self.checkBox_23.setObjectName("checkBox_23")
        self.textEdit_27 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_27.setGeometry(QtCore.QRect(140, 230, 181, 21))
        self.textEdit_27.setObjectName("textEdit_27")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(620, 320, 111, 17))
        self.label_37.setObjectName("label_37")
        self.textEdit_28 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_28.setGeometry(QtCore.QRect(640, 350, 591, 201))
        self.textEdit_28.setStyleSheet("color: rgb(136, 138, 133);")
        self.textEdit_28.setObjectName("textEdit_28")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1240, 350, 151, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_29 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_29.setGeometry(QtCore.QRect(510, 670, 101, 21))
        self.textEdit_29.setObjectName("textEdit_29")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(510, 640, 121, 20))
        self.label_38.setObjectName("label_38")
        self.textEdit_30 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_30.setGeometry(QtCore.QRect(510, 750, 101, 21))
        self.textEdit_30.setObjectName("textEdit_30")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(510, 720, 111, 20))
        self.label_39.setObjectName("label_39")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1250, 390, 131, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1412, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuControl_finger_setting = QtWidgets.QMenu(self.menubar)
        self.menuControl_finger_setting.setObjectName("menuControl_finger_setting")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuIoT_net = QtWidgets.QMenu(self.menubar)
        self.menuIoT_net.setObjectName("menuIoT_net")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionconnect = QtWidgets.QAction(MainWindow)
        self.actionconnect.setObjectName("actionconnect")
        self.actionsetting_network = QtWidgets.QAction(MainWindow)
        self.actionsetting_network.setObjectName("actionsetting_network")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionsave_as)
        self.menuFile.addAction(self.actionQuit)
        self.menuIoT_net.addAction(self.actionconnect)
        self.menuIoT_net.addAction(self.actionsetting_network)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuControl_finger_setting.menuAction())
        self.menubar.addAction(self.menuIoT_net.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
              # Main Robotics Arm 
        file = open("RoboticsScrypt.csv","r")
        InitialVal = file.readlines()   # Read the lines of the value val 
        DataInit = InitialVal[0].split(",")
        DataInit_2 = InitialVal[1].split(",")
        print(DataInit[0])
         # Button for geenerating file and Motion 
        self.pushButton.clicked.connect(self.Functioningcontrol) # Generate file 
        self.pushButton_2.clicked.connect(self.TestMotiondrive)  #Test motion 
        self.pushButton_3.clicked.connect(self.ProcessingMotion) # Processing 
        self.pushButton_4.clicked[bool].connect(self.Teachloopiterator) # Looping teaching mode for the robot 
          # Dial Setting function and knob positioning control  
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(int(DataInit[0]))
        self.dial.valueChanged.connect(self.Basecontrol)
        self.textEdit.setText(str(DataInit[0])) # Display the text on the beginning state 
          # Dial2 Settings 
        self.dial_2.setMinimum(0) 
        self.dial_2.setMaximum(180)
        self.dial_2.setValue(int(DataInit[1]))
        self.dial_2.valueChanged.connect(self.Shouldercontrol)
        self.textEdit_2.setText(str(DataInit[1]))
           # Dial3 Settings 
        self.dial_3.setMinimum(0)
        self.dial_3.setMaximum(180)
        self.dial_3.setValue(int(DataInit[2]))
        self.dial_3.valueChanged.connect(self.Elbowcontrol)
        self.textEdit_3.setText(str(DataInit[2]))
           # Dial4 Settings 
        self.dial_4.setMinimum(0)
        self.dial_4.setMaximum(180) 
        self.dial_4.setValue(int(DataInit[3]))
        self.dial_4.valueChanged.connect(self.RotationFingercont)
        self.textEdit_4.setText(str(DataInit[3]))
           # Dial center assembly Settings using the stepper motor as the actuator    
        self.dial_10.setMinimum(0)      
        self.dial_10.setMaximum(360) 
        self.dial_10.setValue(90)
        self.dial_10.valueChanged.connect(self.Centercontrols)
           # Dial Process time to set the timing for the motioncontrol
        self.dial_9.setMinimum(0)      
        self.dial_9.setMaximum(100) 
        self.dial_9.setValue(0)
        self.dial_9.valueChanged.connect(self.Processingtiming)
           # Hydraulic length adjust 
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(int(DataInit[4]))
        self.horizontalSlider.valueChanged.connect(self.HydraulicAdjustment)
        self.textEdit_5.setText(str(DataInit[4]))

           # Gripper hydraulic adjust
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(180) 
        self.horizontalSlider_2.setValue(int(DataInit[5]))
        self.horizontalSlider_2.valueChanged.connect(self.Gripperhydraulic) 
        self.textEdit_6.setText(str(DataInit[5]))
        self.textEdit_30.setText(str(DataInit[6]))
           # Robotics Arm part bringer  
          # Base part bringer 
        self.dial_5.setMinimum(0)
        self.dial_5.setMaximum(180)
        self.dial_5.setValue(int(DataInit_2[0]))
        self.dial_5.valueChanged.connect(self.Basebringer) # Base parts bringer connected function 
        self.textEdit_8.setText(str(DataInit_2[0]))

          # Shoulder part bringer 
        self.dial_6.setMinimum(0)
        self.dial_6.setMaximum(180)
        self.dial_6.setValue(int(DataInit_2[1]))
        self.dial_6.valueChanged.connect(self.Shoulderbringer)
        self.textEdit_12.setText(str(DataInit_2[1]))

          # Elbow part bringer
        self.dial_7.setMinimum(0)
        self.dial_7.setMaximum(180)
        self.dial_7.setValue(int(DataInit_2[2]))
        self.dial_7.valueChanged.connect(self.Elbowbringer)
        self.textEdit_10.setText(str(DataInit_2[2]))

          # Rotation part bringer
        self.dial_8.setMinimum(0)
        self.dial_8.setMaximum(180)
        self.dial_8.setValue(int(DataInit_2[3]))
        self.dial_8.valueChanged.connect(self.Rotationbringer)
        self.textEdit_11.setText(str(DataInit_2[3]))

          # Hydraulic part bringer 
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setValue(int(DataInit_2[4]))
        self.horizontalSlider_3.valueChanged.connect(self.Hydraulicbringer)
        self.textEdit_9.setText(str(DataInit_2[4]))
        
          #Gripper Part bringer 
        self.horizontalSlider_4.setMaximum(0)
        self.horizontalSlider_4.setMaximum(180)
        self.horizontalSlider_4.setValue(int(DataInit_2[5]))
        self.horizontalSlider_4.valueChanged.connect(self.Gripperbringer)
        self.textEdit_13.setText(str(DataInit_2[5]))
        self.textEdit_29.setText(str(DataInit_2[6]))
             #Tools selector 
        self.checkBox.stateChanged.connect(self.Drillheadtools) # State change selected function 
        self.checkBox_2.stateChanged.connect(self.GripperTools) # Gripper changer 
        self.checkBox_3.stateChanged.connect(self.VacuumTools) # Vacuum Tools 
        self.checkBox_4.stateChanged.connect(self.FluidicTools) # Fluidic Tools 
        self.checkBox_5.stateChanged.connect(self.LaserTools) #Laser tools 
        self.checkBox_6.stateChanged.connect(self.SolderingironTools) # Soldering tools list 
        self.checkBox_7.stateChanged.connect(self.cameraTools) # Camera tools
        self.checkBox_15.stateChanged.connect(self.ColorMixerTools) # Color mixer tools
           # Permission function to tell the robot to know what tools to use on the user application
        self.checkBox_8.stateChanged.connect(self.DrillPermission) # Tools permission selected
        self.checkBox_9.stateChanged.connect(self.GripperPermission) 
        self.checkBox_10.stateChanged.connect(self.VacuumPermission)
        self.checkBox_11.stateChanged.connect(self.FluidPermission)
        self.checkBox_12.stateChanged.connect(self.LaserPermission)
        self.checkBox_13.stateChanged.connect(self.SolderingPermission)
        self.checkBox_14.stateChanged.connect(self.ColormixerPermission)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Assem arms control tech"))
        self.label.setText(_translate("MainWindow", "Base"))
        self.label_3.setText(_translate("MainWindow", "Elbow"))
        self.label_4.setText(_translate("MainWindow", "Rotation finger"))
        self.label_5.setText(_translate("MainWindow", "Hydraulic Linear actuator"))
        self.label_6.setText(_translate("MainWindow", "Gripper actuators "))
        self.label_7.setText(_translate("MainWindow", "Motion generator"))
        self.label_8.setText(_translate("MainWindow", "Shoulder"))
        self.label_9.setText(_translate("MainWindow", "Elbow"))
        self.label_10.setText(_translate("MainWindow", "Rotation finger"))
        self.label_11.setText(_translate("MainWindow", "Base"))
        self.label_12.setText(_translate("MainWindow", "Hydraulic Linear"))
        self.label_13.setText(_translate("MainWindow", "Gripper actuators "))
        self.label_14.setText(_translate("MainWindow", "Initial settings data Main arm "))
        self.pushButton.setText(_translate("MainWindow", "Generate file "))
        self.pushButton_2.setText(_translate("MainWindow", "Test motion"))
        self.pushButton_3.setText(_translate("MainWindow", "Processing "))
        self.label_15.setText(_translate("MainWindow", "Components Process list "))
        self.label_16.setText(_translate("MainWindow", "Process check scheme "))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#729fcf;\">Scripts in</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#729fcf;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Robotics Scripts "))
        self.checkBox.setText(_translate("MainWindow", "Drills"))
        self.checkBox_2.setText(_translate("MainWindow", "Gripper"))
        self.checkBox_3.setText(_translate("MainWindow", "Vacuum"))
        self.checkBox_4.setText(_translate("MainWindow", "Fluidic"))
        self.checkBox_5.setText(_translate("MainWindow", "Laser"))
        self.checkBox_6.setText(_translate("MainWindow", "Sodering iron"))
        self.checkBox_7.setText(_translate("MainWindow", "Camera image processing"))
        self.checkBox_15.setText(_translate("MainWindow", "Color mixer"))
        self.label_18.setText(_translate("MainWindow", "Base"))
        self.label_2.setText(_translate("MainWindow", "Shoulder"))
        self.label_19.setText(_translate("MainWindow", "Shoulder"))
        self.label_20.setText(_translate("MainWindow", "Main arm "))
        self.label_21.setText(_translate("MainWindow", "Elbow"))
        self.label_22.setText(_translate("MainWindow", "Rotation finger"))
        self.label_23.setText(_translate("MainWindow", "Hydraulic Linear actuator"))
        self.label_24.setText(_translate("MainWindow", "Gripper actuators "))
        self.label_25.setText(_translate("MainWindow", "Parts bringer arm"))
        self.label_26.setText(_translate("MainWindow", "Main arm "))
        self.label_27.setText(_translate("MainWindow", "Shoulder"))
        self.label_28.setText(_translate("MainWindow", "Elbow"))
        self.label_29.setText(_translate("MainWindow", "Hydraulic Linear"))
        self.label_30.setText(_translate("MainWindow", "Base"))
        self.label_31.setText(_translate("MainWindow", "Initial settings data part bringer arm "))
        self.label_32.setText(_translate("MainWindow", "Gripper actuators "))
        self.label_33.setText(_translate("MainWindow", "Rotation finger"))
        self.label_34.setText(_translate("MainWindow", "Process time"))
        self.label_35.setText(_translate("MainWindow", "Center assembly "))
        self.label_36.setText(_translate("MainWindow", "Parts Bringer "))
        self.checkBox_8.setText(_translate("MainWindow", "Drills"))
        self.checkBox_9.setText(_translate("MainWindow", "Gripper"))
        self.checkBox_10.setText(_translate("MainWindow", "Vacuum"))
        self.checkBox_11.setText(_translate("MainWindow", "Fluidic"))
        self.checkBox_12.setText(_translate("MainWindow", "Laser"))
        self.checkBox_13.setText(_translate("MainWindow", "Sodering iron"))
        self.checkBox_14.setText(_translate("MainWindow", "Camera image processing"))
        self.checkBox_23.setText(_translate("MainWindow", "Color mixer"))
        self.label_37.setText(_translate("MainWindow", "Process scripts"))
        self.textEdit_28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#729fcf;\">Scripts in</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#729fcf;\"><br /></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Teach robotics arms"))
        self.label_38.setText(_translate("MainWindow", "Arm bringer time"))
        self.label_39.setText(_translate("MainWindow", "Main Arm time "))
        self.pushButton_5.setText(_translate("MainWindow", "Stop Processing "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuControl_finger_setting.setTitle(_translate("MainWindow", "Control finger setting"))
        self.menuhelp.setTitle(_translate("MainWindow", "help "))
        self.menuIoT_net.setTitle(_translate("MainWindow", "IoT net "))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionsave.setText(_translate("MainWindow", "save "))
        self.actionsave_as.setText(_translate("MainWindow", "save as "))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionconnect.setText(_translate("MainWindow", "connect"))
        self.actionsetting_network.setText(_translate("MainWindow", "setting network "))
    def Quitui(self): 
        sys.exit() 
    def Functioningcontrol(self): 
         # Initial value input for testing looping motion iteration 
        BaseMesgI = self.textEdit.toPlainText()+","+self.textEdit_2.toPlainText()+","+self.textEdit_3.toPlainText()+","+self.textEdit_4.toPlainText()+","+self.textEdit_5.toPlainText()+","+self.textEdit_6.toPlainText()+","+self.textEdit_30.toPlainText()
        Partbringer = self.textEdit_8.toPlainText()+","+self.textEdit_12.toPlainText()+","+self.textEdit_10.toPlainText()+","+self.textEdit_11.toPlainText()+","+self.textEdit_9.toPlainText()+","+self.textEdit_13.toPlainText()+","+self.textEdit_29.toPlainText() 
        Processgen = self.textEdit_28.toPlainText() # Process text input for the functional control added 
        file = open("RoboticsScrypt.csv","w+")  # wtite the file name after button 
        print("Generating....") 
        count = 0 
        while count < 100: 
            count +=1 
            time.sleep(0.1) 
            self.progressBar.setValue(count)
            if count == 100: 

                 file.writelines(BaseMesgI)
                 file.writelines(Partbringer)
                 file.writelines(Processgen)
                 print("Generating complete !")
    # Tooling functioning and slection detail 
             # Gripper 
    def Drillheadtools(self,state):
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[6].split(",")
            ToolsDatlist = Toolsdata[7].split(",")
            self.textEdit_14.setText(str(ToolsDatanum))
            print("Drill Tools list "+str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
        else:
            self.textEdit_14.setText(" ")
            #self.textEdit_28.setText("")  
    def GripperTools(self,state):
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[8].split(",")
            ToolsDatlist = Toolsdata[9].split(",")
            self.textEdit_15.setText(str(ToolsDatanum))
            print("Gripper Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
       else:
            self.textEdit_15.setText(" ")
    def VacuumTools(self,state): 
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[10].split(",")
            ToolsDatlist = Toolsdata[11].split(",")
            self.textEdit_16.setText(str(ToolsDatanum)) 
            print("Vacuum Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
        else:
            self.textEdit_16.setText(" ") 
    def FluidicTools(self,state): 
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[12].split(",")
            ToolsDatlist = Toolsdata[13].split(",")
            self.textEdit_17.setText(str(ToolsDatanum)) 
            print("Fluidic Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
        else:
            self.textEdit_17.setText(" ") 
    def LaserTools(self,state): 
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[14].split(",")
            ToolsDatlist = Toolsdata[15].split(",")
            self.textEdit_18.setText(str(ToolsDatanum)) 
            print("Fluidic Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
        else:
            self.textEdit_18.setText(" ") 
    def SolderingironTools(self,state): 
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[16].split(",")
            ToolsDatlist = Toolsdata[17].split(",")
            self.textEdit_19.setText(str(ToolsDatanum)) 
            print("Fluidic Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
        else:
            self.textEdit_19.setText(" ") 
    def cameraTools(self,state):   
         if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[18].split(",")
            ToolsDatlist = Toolsdata[19].split(",")
            self.textEdit_26.setText(str(ToolsDatanum)) 
            print("Camera Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
         else:
            self.textEdit_26.setText(" ") 
    def ColorMixerTools(self,state): 
         if (QtCore.Qt.Checked == state):
            file = open("RoboticsScrypt.csv","r") # Read and open to the settings
            Toolsdata = file.readlines()
            ToolsDatanum = Toolsdata[20].split(",")
            ToolsDatlist = Toolsdata[21].split(",")
            self.textEdit_27.setText(str(ToolsDatanum)) 
            print("Color Tools list "+ str(len(ToolsDatlist)))
            for i in range(0,len(ToolsDatlist)): 
               self.textEdit_28.setText("\n"+ str(ToolsDatlist[i])) 
               print("\n" + str(ToolsDatlist[i]))
               time.sleep(0.2)
         else:
            self.textEdit_27.setText(" ") 
   #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # Tools slector 
    def DrillPermission(self,state):  # Check slected drill tools 
         if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Drillpermitted")
         else:
            print("Drill not permitted") 
    def GripperPermission(self,state): 
        if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Gripperpermitted")
        else:
            print("Gripper not permitted") 
    def VacuumPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Vacuumpermitted")
       else:
            print("Vacuum not permitted") 
    def FluidPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Drillpermitted")
       else:
            print("Fluidtools not permitted")        
    def LaserPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Laserpermitted")
       else:
            print("Laser not permitted")
    def SolderingPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Solderingmitted")
       else:
            print("Soldering not permitted") 
    def CameraPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Laserpermitted")
       else:
            print("Laser not permitted") 
    def ColormixerPermission(self,state): 
       if (QtCore.Qt.Checked == state):
            file = open("RoboticsProcess.csv","w") # Read and open to the settings
            file.writelines("Colormixerpermitted")
       else:
            print("Colormixer not permitted") 

    def TestMotiondrive(self):
      file = open("RoboticsScrypt.txt","r")
      Lang = file.readlines() 
      LengtEven = Lang[2].split(",")
      print(len(LengtEven))
      count = 0 
      while count < len(LengtEven)*10: 
            count +=1 
            time.sleep(0.08) 
            self.progressBar_2.setValue(count)
            if count == len(LengtEven)*10: 
                 Text = open("RoboticsScrypt.txt").read()
                 file = open("RoboticsScrypt.csv","r")
                 InitialAngle = file.readlines()
                 PartData = InitialAngle[0].split(",")
                 PartData2 = InitialAngle[1].split(",")
                 PartData3 = InitialAngle[2].split("=")
                 PartData4 = InitialAngle[3].split(",")
                 PartData5 = InitialAngle[4].split(",")
                 PartData6 = InitialAngle[5].split(",")
                 Colormixerdata = PartData3[1]
                 print(PartData[0])
                 print(PartData2[0])
                 print(PartData3[0])
                 self.textEdit_28.setText(PartData3[0]+"="+PartData3[1]+str(PartData4)+str(PartData5)+str(PartData6))       
                 self.textEdit_7.setText(Text + "\n" + str(PartData) +"\n" + str(PartData2))
                 file = open("RoboticsScrypt.txt","r") 
                 mesg = file.readlines() # Read the raw text from the file scrypt 
                 scryptsRoot = mesg[2].split(",")
                 BaseMesgScrypt = "Parts"+"\t"+scryptsRoot[0] +"\t" + "Angle:"+scryptsRoot[1]
                 ShoulderMesgScrypt =  "Parts"+"\t"+scryptsRoot[2] +"\t" + "Angle:"+scryptsRoot[3]
                 ElbowMesgScrypt = "Parts"+"\t"+scryptsRoot[4] +"\t" + "Angle:"+scryptsRoot[5]
                 RotationFMesgScrypt =  "Parts"+"\t"+scryptsRoot[6] +"\t" + "Angle:"+scryptsRoot[7]
                 TimingMesgScrypt =  "Parts"+"\t"+scryptsRoot[8] +"\t" + "Angle:"+scryptsRoot[9]
                 print("Read from scripts")
                 print("\n" + BaseMesgScrypt)
                 print("\n" + ShoulderMesgScrypt)
                 print("\n" + ElbowMesgScrypt)
                 print("\n"+RotationFMesgScrypt)
                 print("\n"+TimingMesgScrypt)
                 print("\n"+str(Colormixerdata))
                 

                # teach loop command to looping iteration 
    def Teachloopiterator(self):
        Ebutton = ElectronicsButton.read()  # Digital read mode for the teaching button 
        # Analog read sensors  
        hardware.analog[0].read()
        hardware.analog[1].read()
        hardware.analog[2].read()
        hardware.analog[3].read()
        hardware.analog[4].read()
        hardware.analog[5].read()  
        print("Teach process begin !")     
        while str(Ebutton) == True:
               # Teaching re write Script on it own
              file = open("RoboticsScrypt.txt","w")  # Write down the sensor file  
               # Arm1 write sensor angle in raw value 
              file.write("\n"+"Base"+","+str(hardware.analog[0].read())+","+"Shoulder"+","+str(hardware.analog[1].read())+","+ "Elbow"+","+str(hardware.analog[2].read()) +","+ "Rotatefinger"+","+str(hardware.analog[3].read())+","+"Hydraulic linear"+","+str(hardware.analog[4].read())+","+"Gripper"+","+str(hardware.analog[5].read()))
                 # All angle functioning feed back Script 
              BaseAngle = (((hardware.analog[0].read())*500)*180)/1024
              ShoulderAngle = (((hardware.analog[1].read())*500)*180)/1024
              ElbowAngle = (((hardware.analog[2].read())*500)*180)/1024
              RotateFingerAngle = (((hardware.analog[3].read())*500)*180)/1024
              HydraulicLinear = (((hardware.analog[4].read())*500)*180)/1024
              GripperAngle = (((hardware.analog[5].read())*500)*180)/1024 
              file.writelines("\n"+"Base"+","+str(BaseAngle)+","+"Shoulder"+","+str(ShoulderAngle)+","+"Elbow"+","+str(ElbowAngle)+","+"Rotationfinger"+","+str(RotateFingerAngle)+","+"Hydrauliclinear"+","+str(HydraulicLinear)+","+"Gripper"+","+str(GripperAngle))
                    
    def ProcessingMotion(self): 
              # Read out the file and processing the scrypt 
      file = open("RoboticsScrypt.txt","r")
      Lang = file.readlines() 
      LengtEven = Lang[2].split(",")
      print(len(LengtEven))
      count = 0 
      while count < len(LengtEven)*10: 
            count +=1 
            time.sleep(0.08) 
            self.progressBar_3.setValue(count)
            #if count == len(LengtEven)*10: 
    def Basecontrol(self):
        print("Base angle value = %i" % (self.dial.value()))
        blink.write(self.dial.value()/100)  # Hardware linking control brigtness of the LED test 
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
        Base.write(self.dial.value())
        
    def Shouldercontrol(self): 
        print("Shoulder angle value = %i" %(self.dial_2.value()))
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
        Shoulder.write(self.dial_2.value())
    def Elbowcontrol(self):
           Angleelbow = self.dial_3.value() 
           errorElbow = hardware.analog[0].read() 
           print("AngleElbow sensor" + "\t\t"+str(errorElbow*500))
           print("AngleElbow control" +"\t\t" +str(Angleelbow))
           file = open("RoboticsScrypt.txt","w+")
           file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
           if Angleelbow == errorElbow: 
              ElbowL.write(0)
              ElbowR.write(0)
           if Angleelbow > errorElbow: 
              ElbowL.write(10)
              ElbowR.write(0)
           if Angleelbow < errorElbow: 
              ElbowL.write(0)
              ElbowR.write(10) 
    def RotationFingercont(self): 
           print("Rotationfinger angle %i" %(self.dial_4.value()))
           file = open("RoboticsScrypt.txt","w+")
           file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
    def AddToolscom(self):         
          file = open("RoboticsScrypt.txt","a+")
          print("Adding the tooling machine to the robotics Arms")
          
    def AnalogRead(self): 
        for _ in itertools.count():
             AnalogReadA1 = hardware.analog[0].read()
             self.progressBar_2.setValue(AnalogReadA1*500) 
             print(AnalogReadA1)
    def Centercontrols(self):   # Turning degree for the center assembly 
        Turningangle = self.dial_10.value()
        print("Angle center degree turning %i" %(self.dial_10.value()))
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
        
    def Processingtiming(self): 
        Processingtiming = self.dial_9.value() 
        self.lcdNumber.display(Processingtiming/100) # Processing timing 
        print("timing %i" %(self.dial_9.value()) + "millisec")
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"HydraulicLinear"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
    def HydraulicAdjustment(self): 
        Length = self.horizontalSlider.value() 
        print("Length value %i" %Length)
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
    def Gripperhydraulic(self): 
        Gripped = self.horizontalSlider_2.value() 
        print("Gripper Angle %i" %Gripped) 
        file = open("RoboticsScrypt.txt","w+")
        file.writelines("\n\n" + "Base" +","+str(self.dial.value()) +","+ "Shoulder"+ ","+str(self.dial_2.value())+","+"Elbow"+","+str(self.dial_3.value())+","+"Rotfingers"+","+str(self.dial_4.value())+","+"timing"+","+str(self.dial_9.value()) +","+"CenterAssembly"+str(self.dial_10.value())+","+"Hydraulicunit"+","+str(self.horizontalSlider.value())+","+"GripperActuators"+","+str(self.horizontalSlider_2.value()))
        # Robotics Arm Part bringer 
    def Basebringer(self): 
       Basebringerval = self.dial_5.value() 
       print("Base bringer angle%i" %(self.dial_6.value()))
    def Shoulderbringer(self): 
       Shoulderbringerval = self.dial_6.value() 
       print("Shoulder bringer angle %i" %(self.dial_6.value()))
    def Elbowbringer(self): 
       Elbowbringerval = self.dial_7.value()
       print("Elbow bringer angle %i" %(self.dial_7.value()))
    def Rotationbringer(self): 
       Rotationbringerval = self.dial_8.value()
       print("Rotation bringer angle %i" %(self.dial_8.value()))
    def Hydraulicbringer(self):
         HydraulicLinearval = self.horizontalSlider_3.value() 
         print("Hydraulic linear %i" %(self.horizontalSlider_3.value()))
    def Gripperbringer(self): 
         Gripperbringerval = self.horizontalSlider_4.value() 
         print("Gripperbringerval %i" %(self.horizontalSlider_4.value()))      
    

if __name__ == "__main__":
    import sys
    try: 
      hardware = pyfirmata.ArduinoMega("COM4")
      print("Hardware robotics assembly line connected successfully !")   
    except: 
      print("Hardware connection fail please reconnect and check connection port !")
    it = pyfirmata.util.Iterator(hardware)
    it.start() 
            # Main Assembly arm 
    blink = hardware.get_pin('d:13:p')
    Base = hardware.get_pin('d:2:s')
    Shoulder = hardware.get_pin('d:3:s')  # using the servo circuit driver with new  planetary gear 
    ElbowL = hardware.get_pin('d:4:p')
    ElbowR = hardware.get_pin('d:5:p')
    Wrist  = hardware.get_pin('d:6:s') 
    #HydraulicLinearL = hardware.get_pin('d:7:p')
    #HydraulicLinearR = hardware.get_pin('d:8:p') 
    Rotatefingers = hardware.get_pin('d:9:s')
    Grippers = hardware.get_pin('d:10:s')  
    CenterAssembly  = hardware.get_pin('d:11:s') # Assembly platform to attach the  work pieces on the assembly 
           # Robotics Arm parts bringer 
    Base1 = hardware.get_pin('d:12:s')
    Shoulder1 = hardware.get_pin('d:14:s')  # using the servo circuit driver with$
    Elbow1L = hardware.get_pin('d:20:s')
    Elbow1R = hardware.get_pin('d:16:s')
    Wrist1  = hardware.get_pin('d:17:s') 
    #HydraulicLinear1L = hardware.get_pin('d:18:p')
    #HydraulicLinear1R = hardware.get_pin('d:19:p') 
    Rotatefinger1s = hardware.get_pin('d:21:s')
    Grippers1 = hardware.get_pin('d:22:s')  
    ElectronicsButton = hardware.get_pin('d:23:i') 
    hardware.analog[0].enable_reporting()
    hardware.analog[1].enable_reporting()
    hardware.analog[2].enable_reporting()
    hardware.analog[3].enable_reporting()
    hardware.analog[4].enable_reporting()
    hardware.analog[5].enable_reporting() 
    ElectronicsButton.enable_reporting() # Report electronics buttons 

    #AnalogReadA1 = hardware.analog[0].read()    
    
    time.sleep(0.1)
    for i in range(0,10):
       blink.write(i)
       time.sleep(0.2)
    time.sleep(0.1)   
    for i in range(0,10,-1):
       blink.write(i)
       time.sleep(0.2)    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
