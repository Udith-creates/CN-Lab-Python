import socket
s = socket.socket()
s.bind(('localhost', 8001))
s.listen(1)
c, addr = s.accept()
data = c.recv(1024)
c.send(data) # Echo
c.close()