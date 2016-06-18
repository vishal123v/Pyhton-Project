import sys
from PyQt4 import QtCore, QtGui
from time import sleep
from pyfile import Ui_MainWindow


class workerThread(QtCore.QThread):
	def __init__(self,parent=None):
		QtCore.QThread.__init__(self,parent)
		self.signal = QtCore.SIGNAL("signal")
	def run(self):
		while True:
			self.emit(self.signal)#emitting signal->
			
			#print "signal"
			sleep(0.5)

class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.t=workerThread()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.button.clicked.connect(self.emit_signal)#click->going to emit_signal
		self.connect(self.t, self.t.signal, self.update_widget)

		#self.t.start()
		self.flag=False
	def update_widget(self):

		self.ui.tv.insertPlainText("hi\n")#slot
	def emit_signal(self):#to start worker thread
		self.flag= not self.flag
		if self.flag:
			self.t.start()
		else:
			self.t.terminate()#to terminate,stop printing
			self.ui.tv.clear()#to clear text edit



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())

