import socket
from threading import Thread
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect(('127.0.0.1',port))
print "rasberrypi data:"
def recv():
	global s
	while 1:
		print "waiting for recieve"
		reply=s.recv(1024)
		print "from server :",reply
		if reply=='q':
			break
			s.close()	
def send():
	while 1:
		ip=raw_input("client:",)
		s.send(ip)
		if ip=='q':
			break
		s.close()
t1=Thread(target=send)
t2=Thread(target=recv)
t1.start()
t2.start()
s.close()
