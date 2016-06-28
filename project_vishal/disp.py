# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj.ui'
#
# Created: Tue Jun 28 16:40:36 2016
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
        MainWindow.resize(424, 402)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table1 = QtGui.QTableWidget(self.centralwidget)
        self.table1.setGeometry(QtCore.QRect(110, 140, 201, 171))
        self.table1.setObjectName(_fromUtf8("table1"))
        self.table1.setColumnCount(2)
        self.table1.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, item)
        self.table2 = QtGui.QTableWidget(self.centralwidget)
        self.table2.setGeometry(QtCore.QRect(110, 50, 201, 61))
        self.table2.setObjectName(_fromUtf8("table2"))
        self.table2.setColumnCount(2)
        self.table2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "APP", None))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature", None))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature", None))

