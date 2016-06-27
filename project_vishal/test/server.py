import socket
from threading import Thread
from time import sleep
import sys
s=socket.socket()
host='127.0.0.1'
port=1234
s.bind(('127.0.0.1',port))
s.listen(1)
c,addr=s.accept()
print "connected:"
ip=0
op=0
def send():
	global c,s,ip,op
	while 1:

		ip=raw_input("server :")
		c.send(ip)
		if ip=='q' or op=='q':
			try:
				c.send('q')
			except Exception, e:
				print 'send 1:', e
			s.close()
			break
def recv():
	global c,s
	while 1:
		op=c.recv(1024)
		print "rasberry: ", op
		if ip=='q' or op=='q':
			try:
				c.send('q')
			except Exception, e:
				print 'recv 2:', e
				break
		s.close()
t1=Thread(target=send)
t2=Thread(target=recv)
t1.start()
t2.start()
s.close()
