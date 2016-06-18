import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect(('127.0.0.1',port))
while 1:

	reply=s.recv(1024)
	print "from server ",reply
	if reply=='q':
		break
	ip=raw_input("strt chat:",)
	s.send(ip)
	if ip=='q':
		break
s.close()