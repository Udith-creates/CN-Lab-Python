import socket
s = socket.socket()
s.connect(('localhost', 8001))
s.send(b"Hello World")
print(s.recv(1024).decode())
s.close()