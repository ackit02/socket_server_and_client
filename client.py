import socket
import random
old_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    try:
        old_socket.bind(("192.168.1.23", random.randint(1001, 65335)))
        break
    except:
        None
old_socket.connect(("192.168.1.23", 8000))
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
random_port = 0
while 1:
    try:
        random_port = random.randint(1001, 65535)
        new_socket.bind(("192.168.1.23", random_port))
        break
    except:
        None
if old_socket.recv(1024).decode("UTF-8") == 'ok':
    old_socket.send(str(random_port).encode("UTF-8"))
new_socket.listen(5)
conn, addr = new_socket.accept()
conn.send("Sonya".encode("UTF-8"))
while 1:
    conn.send(input(">").encode("UTF-8"))