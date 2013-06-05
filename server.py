import socket
from threading import Thread

def clientHandler():
	conn, addr = serversock.accept()
	print addr, "is connected"
	while True:
		data = conn.recv(1024)
		if not data:
			break
		print "Receive message:" repr(data)

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(('', 8000))
serversock.listen(5)

for i in range(5):
	Thread(target = clientHandler).start()

serversock.close

