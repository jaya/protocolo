import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input()
        size = chr(len(msg))
        s.send(size.encode())
        s.send(msg.encode())
        response = s.recv(1)
        size = response[0]
        response = s.recv(size)
        print(response.decode())
