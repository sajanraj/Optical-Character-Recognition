# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from secondscreen import Ui_Form
from pancheck import ocr




class Ui_MainWindow(object):

    def screen2(self,MainWindow):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpg *jpeg *.bmp)")

        text,outflag = ocr(fileName,'name','thresh')
        MainWindow.hide()
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form,MainWindow,[fileName,text])
        self.Form.show()

    def setupUi(self, MainWindow):
        icon = QtGui.QIcon('dat.png')
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("Text Extractor")
        MainWindow.resize(559, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.mainlabel.setFont(font)
        self.mainlabel.setObjectName("mainlabel")
        self.verticalLayout.addWidget(self.mainlabel)
        self.extractbtn = QtWidgets.QPushButton(self.centralwidget)
        self.extractbtn.setObjectName("extractbtn")
        self.verticalLayout.addWidget(self.extractbtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.extractbtn.clicked.connect(lambda:self.screen2(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainlabel.setText(_translate("MainWindow", "Charactor Recognition System"))
        self.extractbtn.setText(_translate("MainWindow", "Extract"))




