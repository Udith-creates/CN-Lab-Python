
import socket
s = socket.socket()
s.bind(('localhost', 8800))
s.listen(1)
c, addr = s.accept()
f = open('test.txt', 'rb')
c.send(f.read()) # Sends entire file at once
f.close()
c.close()