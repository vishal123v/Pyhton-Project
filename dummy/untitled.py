#!/usr/bin/env python
"""This is a short program to have an external program grab data for me and get displayed without blocking the whole program"""
from PyQt4 import QtGui,QtCore
import sys
class TerminalViewer(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.Label = QtGui.QLabel("Waiting for Something",self)
		self.thread_obj = thread(self)
		self.connect(self.thread_obj,QtCore.SIGNAL("Activated ( QString ) "), self.Activated)
		self.thread_obj.start()
	def Activated(self,newtext):
		self.Label.setText(newtext)
	def closeEvent(self,e):
		e.accept()
		app.exit()

class thread(QtCore.QThread):
	def __init__(self,parent=None):
		QtCore.QThread.__init__(self,parent)
		self.test = ''
	def run(self):
		while self.test != 'q':
			self.test = raw_input('enter data: ')
			self.emit(QtCore.SIGNAL("Activated( QString )"),self.test)

app = QtGui.QApplication(sys.argv)
qb = TerminalViewer()
qb.show()
sys.exit(app.exec_())