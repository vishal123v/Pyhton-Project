import socket
from time import strftime
s=socket.socket()
s.connect(("127.0.0.1",1234))
def send():
	global s
	while 1:
		temp=raw_input(">")
		data=strftime("%d-%m-%Y %I:%M:%S")+','+temp
		print data
		s.send(data)
		if temp=='q':
			break
	
try:
	send()
finally:
	s.close()
