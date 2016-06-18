import threading
from time import sleep
x=0
def hello():
	global x
	while x!='k':
		print "hello world"
		sleep(0.5)
		'''if x=='k':
			print "\t\tQuit"'''
		

t1=threading.Thread(target=hello)
t1.start()
x=raw_input() 

