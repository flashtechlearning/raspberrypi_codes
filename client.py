import socket

s = socket.socket()

host = '192.168.1.2'
port = 12345

s.connect((host,port))

print(s.recv(1024))
s.close()
