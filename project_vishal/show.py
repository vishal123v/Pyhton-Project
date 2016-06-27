import sys
from PyQt4 import QtCore, QtGui
from time import sleep
from disp import Ui_MainWindow



class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.Button1.clicked.connect(self.emit_signal)
	def emit_signal(self):
		self.ui.table1.setRowCount(1)
		self.ui.table1.setItem(0,0,QtGui.QTableWidgetItem("1"))
		self.ui.table1.setItem(0,1,QtGui.QTableWidgetItem("12-06-2016"))
		self.ui.table1.setItem(0,2,QtGui.QTableWidgetItem("100"))



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
