import socket
s = socket.socket()
s.connect(('localhost', 8800))
f = open('received.txt', 'wb')
f.write(s.recv(4096)) # Increase buffer to catch the file
f.close()
s.close()