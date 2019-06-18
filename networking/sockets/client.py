import socket

sock = socket.socket()
Host = 'localhost'
Port = 9090
sock.connect((Host, Port))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print(data.decode())
