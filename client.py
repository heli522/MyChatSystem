import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(('', 8000))