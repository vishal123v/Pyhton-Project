import socket
import sqlite3
from time import strftime
from configsql import db
s=socket.socket()
s.bind(("127.0.0.1",1234))
s.listen(1)
cl,ip = s.accept()
while 1:
	rec=cl.recv(1024)
	
	if rec=='q':
		s.close()
		break
	try:
		db.insert(strftime("%d-%m-%Y %I:%M:%S"),int(rec))
	except Exception, e:
		print "Error: ", e
	print rec
s.close()