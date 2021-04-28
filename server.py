import socket
import time
s = socket.socket()

host = '192.168.1.2'
port = 12345

s.bind((host, port))

s.listen(5)

while True:
    c , address = s.accept()
    print('Got connection from : ' , address)
    c.send('Successful Connection')
    c.close()

    time.sleep(15)
    break

s.close()
