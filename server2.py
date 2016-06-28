import socket
from threading import Thread
from time import sleep
import sys

s=socket.socket()
host='127.0.0.1'
port=1234
s.bind(('127.0.0.1',port))
s.listen(1)
print "waiting for connection "
c,addr=s.accept()
print "conectted "
ip=0
op=0
def send():
	global c,s,ip,op
	try:
		while 1:	
			ip=raw_input("server:")
			if ip=='q' or op=='q':
				
				try:
					c.send('q')
				except Exception, e:
					print 'send 1:', e
				
				#s.close()
				break

			try:
				c.send(ip)
			except Exception, e:
					print 'send 2:', e
			sleep(0.5)
	finally:
		print 'finally block'
		#s.close()
	print "send done"

def recv():
	global c,s
	try:
		while 1:
			try:
				op=c.recv(1024)
			except Exception, e:
				print 'recv 1:', e
			print op
			if ip=='q' or op=='q':
				try:
					c.send('q')
				except Exception, e:
					print 'recv 2:', e
				#s.close()
				break
			sleep(0.5)
	finally:
		print 'finally block'
		#s.close()
	print "recv done"
t1=Thread(target=send)
t2=Thread(target=recv)
t1.start()
t2.start()
s.close()

