import socket
s=socket.socket()
s.connect(("127.0.0.1",1234))
while 1:
	data=raw_input(">")
	s.send(data)

	if data=='q':
		break

s.close()
