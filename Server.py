import threading
import socket
import random
#this is function for theard, that mean that it should work multiply times
def connection(conne,addr):
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#I'm trying binding excited socket with my local ip and random port
    while 1:
        try:
            new_socket.bind((socket.gethostbyname(socket.gethostname()), random.randint(1001, 65335)))
            break
        except:
            None
#Server sending this message to make show, that server is ready to recv new port from client 
    conne.send("ok".encode("UTF-8"))
    port = int(conn.recv(1024).decode("UTF-8"))
    address = (addr[0], port)
#server making new socket for future connecting with client and to make free excited socket
    new_socket.connect(address)
    nickname = new_socket.recv(1024).decode("UTF-8")
#Close connecting with "old" socket, now server is ready to accept new connection
    conn.close()
    print(f"User {nickname} already connected")
#This variable show that function is already close connecting
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
    sock.bind((socket.gethostbyname(socket.gethostname()), 8000))
#Server make standart socket with constant port
    sock.listen(5)
    conn, addr = sock.accept()
#Now new theard taking socket and function "connection"
    xs = threading.Thread(target=connection, args=(conn, addr))
    xs.start()
#With loop Server waiting before it can accept new connection 
    while 1:
        if x == 1:
            x = 0
            break
        else:
            None
