import socket

HOST = 'localhost'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input()
        size = str(len(msg))
        s.send(size.encode())
        s.send(msg.encode())
        response = s.recv(1024)
        print(response.decode())
