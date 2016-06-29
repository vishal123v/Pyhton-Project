import socket
import sqlite3
import threading
from sql_config import db
from time import sleep
flag=1
try:
	db.create_table()
except sqlite3.OperationalError, e:
	print e
def send_show():
	s1=socket.socket()
	s1.bind(("127.0.0.1",12345))
	s1.listen(1)
	cl1,ip1=s1.accept()
	try:
		tempr='dummy'
		while flag:
			try:
				date1,temp1=db.get()
				if tempr==date1:
					continue
				print date1,temp1
				cl1.send(date1+','+str(temp1))
				sleep(0.5)
				tempr=date1
			except Exception as e:
				print "No data in table"
				sleep(5)
			
	finally:
		s1.close()
	
def recv_data():
	s=socket.socket()
	s.bind(("127.0.0.1",1234))
	s.listen(1)
	cl,ip = s.accept()

	#global cl
	try:
		while 1:
			global flag
			rec=cl.recv(1024)
			date,temp=rec.split(',')
			if temp=='q' :
				flag=0
				break
			db.insert(date,temp)
			if not rec:
				break
			#print rec
		#sleep()
	finally:
		s.close()

t1=threading.Thread(target=recv_data)
t2=threading.Thread(target=send_show)
t1.start()
t2.start()

	
	
