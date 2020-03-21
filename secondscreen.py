# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seconscreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form,MainWindow,ocr):
        Form.setObjectName("Form")
        Form.resize(600, 460)
        icon = QtGui.QIcon("sajanimage_with_boxes.jpg")
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.verticalLayout.addWidget(self.Image)
        self.TextEdit = QtWidgets.QTextEdit(Form)
        self.TextEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.TextEdit.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.TextEdit)
        self.exitbtn = QtWidgets.QPushButton(Form)
        self.exitbtn.setObjectName("exitbtn")
        self.verticalLayout.addWidget(self.exitbtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.exitbtn.clicked.connect(lambda :self.closewin(MainWindow,Form))
        pixmap = QtGui.QPixmap(ocr[0])  # Setup pixmap with the provided image
        pixmap = pixmap.scaled(640,480,
                               QtCore.Qt.KeepAspectRatio)  # Scale pixmap
        self.Image.setPixmap(pixmap)  # Set the pixmap onto the label
        self.Image.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center
        self.TextEdit.clear()  # Clear the text
        self.TextEdit.append(ocr[1])
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exitbtn.setText(_translate("Form", "Exit"))

    def closewin(self,MainWindow,Form):
        MainWindow.show()
        Form.hide()




