# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI(object):
    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(400, 300)
        UI.setAutoFillBackground(True)
        UI.setStyleSheet("")
        self.comboBox = QtWidgets.QComboBox(UI)
        self.comboBox.setGeometry(QtCore.QRect(250, 60, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(UI)
        self.label.setGeometry(QtCore.QRect(250, 30, 55, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(UI)
        self.textEdit.setGeometry(QtCore.QRect(250, 90, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(UI)
        self.pushButton.setGeometry(QtCore.QRect(250, 130, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(UI)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(UI)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UI)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 121, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(UI)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(UI)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 190, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(UI)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 250, 141, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, UI):
        _translate = QtCore.QCoreApplication.translate
        UI.setWindowTitle(_translate("UI", "Dialog"))
        self.label.setText(_translate("UI", "Numbers:"))
        self.pushButton.setText(_translate("UI", "Set Text"))
        self.label_2.setText(_translate("UI", "Enter you text"))
        self.label_3.setText(_translate("UI", "Display text:"))
        self.pushButton_2.setText(_translate("UI", "Set text"))
        self.pushButton_3.setText(_translate("UI", "Move to Next Window"))
