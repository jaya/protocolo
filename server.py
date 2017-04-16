import socket

HOST = '127.0.0.1'
PORT = 8081

counter = 0


def handle(message):
    global counter
    if message.startswith('GET'):
        return ('O contador está em %i' % counter)
    elif message.startswith('ADD'):
        add = int(message.split()[1])
        counter = counter + add
        return ('O contador foi de %i para %i' % (counter - add, counter))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1)
            size = int(data.decode())
            data = conn.recv(size).decode()
            response = handle(data)
            conn.sendall(response.encode())
