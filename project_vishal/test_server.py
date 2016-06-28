import socket
import sqlite3
import threading
from sql_config import db
from time import sleep

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
		while 1:
			date1,temp1=db.get()
			print date1,temp1
			cl1.send(date1+','+str(temp1))
			sleep(0.5)
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
			rec=cl.recv(1024)
			date,temp=rec.split(',')
			if temp=='q' :
				break
			db.insert(date,temp)
			if not rec:
				break
			print rec
		#sleep()
	finally:
		s.close()

t1=threading.Thread(target=recv_data)
t2=threading.Thread(target=send_show)
t1.start()
t2.start()

	
	
