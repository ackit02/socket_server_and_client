import threading
import socket
import random
def connection(conne,addr):
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while 1:
        try:
            new_socket.bind(("192.168.1.23", random.randint(1001, 65335)))
            break
        except:
            None
    conne.send("ok".encode("UTF-8"))
    port = int(conn.recv(1024).decode("UTF-8"))
    address = (addr[0], port)
    new_socket.connect(address)
    nickname = new_socket.recv(1024).decode("UTF-8")
    conn.close()
    print(f"User {nickname} already connected")
    global x
    x = 1
    while 1:
        message = new_socket.recv(1024)
        try:
            print(f"{nickname}:{message.decode('UTF-8')}")
        except:
            None
x = 0
while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.23", 8000))
    sock.listen(5)
    conn, addr = sock.accept()
    xs = threading.Thread(target=connection, args=(conn, addr))
    xs.start()
    while 1:
        if x == 1:
            x = 0
            break
        else:
            None