import socket
s=socket.socket()
host='127.0.0.1'
port=1234
s.bind(('127.0.0.1',port))
s.listen(1)
c,addr=s.accept()
while 1:
	ip=raw_input("server:")
	c.send(ip)
	if ip=='q':
		s.close()
		break
	op=c.recv(1024)
	print op
	if op=='q':
		s.close()
		break
#s.close()
