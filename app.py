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
			self.emit(self.signal, "hi from thread\n")
			sleep(0.5)

class MyForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.t = workerThread()
		self.connect(self.t, self.t.signal, self.disp)
		self.t.start()
	
	def disp(self, text):
		self.ui.tv.insertPlainText(text)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())