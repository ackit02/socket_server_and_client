import socket
import random
#Making standart socket and trying to bind it with local ip and random port
old_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    try:
        old_socket.bind((socket.gethostbyname(socket.gethostname()), random.randint(1001, 65335)))
        break
    except:
        None
old_socket.connect(("192.168.1.23", 8000))
#Making new socket for future connection
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
random_port = 0
#Same way to binding as first socket
while 1:
    try:
        random_port = random.randint(1001, 65535)
        new_socket.bind(("192.168.1.23", random_port))
        break
    except:
        None
#Waiting when server will be ready for future connection
while 1:
    if old_socket.recv(1024).decode("UTF-8") == 'ok':
    #Sending port of new socket for connection
        old_socket.send(str(random_port).encode("UTF-8"))
        break
    else:
        None
#Waiting when server will connection to client
new_socket.listen(5)
conn, addr = new_socket.accept()
#Just send nickname for to test how server work
conn.send("Sonya".encode("UTF-8"))
while 1:
    conn.send(input(">").encode("UTF-8"))
