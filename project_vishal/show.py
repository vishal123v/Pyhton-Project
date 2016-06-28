import sys
from PyQt4 import QtCore, QtGui
from time import sleep
from disp import Ui_MainWindow
import socket
from enduser_db import db

db.create_table()

class main_Thread(QtCore.QThread):
	def __init__(self,parent=None):
		QtCore.QThread.__init__(self,parent)
		self.s1=socket.socket()
		self.s1.connect(("127.0.0.1",12345))
		self.signal = QtCore.SIGNAL("signal")
	def run(self):
		print "in run main_Thread"
		while 1:
			print "waitinng recv main_Thread"
			rec1=self.s1.recv(1024)
			date,temp=rec1.split(',')
			db.insert(date,temp)
			#print rec1.split(',')
			self.emit(self.signal)





class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.t=main_Thread()
		self.t.start()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connect(self.t,self.t.signal,self.table_disp)

	def table_disp(self):
		self.ui.table2.setRowCount(1)
		date1,temp1=db.get()
				
		
		self.ui.table2.setItem(0,0,QtGui.QTableWidgetItem(date1))
		self.ui.table2.setItem(0,1,QtGui.QTableWidgetItem(str(temp1)))
		



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
	
	
