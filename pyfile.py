# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disp.ui'
#
# Created: Sat Jun 18 11:41:04 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 317)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.text1 = QtGui.QTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(130, 80, 311, 141))
        self.text1.setObjectName(_fromUtf8("text1"))
        self.button1 = QtGui.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(260, 230, 85, 26))
        self.button1.setObjectName(_fromUtf8("button1"))
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(620, 170, 85, 26))
        self.button2.setObjectName(_fromUtf8("button2"))
        self.line1 = QtGui.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(530, 130, 251, 25))
        self.line1.setObjectName(_fromUtf8("line1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button1.setText(_translate("MainWindow", "OK", None))
        self.button2.setText(_translate("MainWindow", "PRESS", None))

