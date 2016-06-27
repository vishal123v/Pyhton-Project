import socket
from threading import Thread
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect(('127.0.0.1',port))
def recv():
	global s
	try:
		while 1:
			print "waiting for recieve"
			reply=s.recv(1024)
			print "from server :",reply
			if reply=='q':
				break
	finally:
		print 'finally block'
		s.close()	
def send():
	global s
	try:
		while 1:			
			ip=raw_input("client:",)
			s.send(ip)
			if ip=='q':
				break
	finally:
		print 'finally block'
		s.close()	
t1=Thread(target=send)
t2=Thread(target=recv)
t1.start()
t2.start()
s.close()