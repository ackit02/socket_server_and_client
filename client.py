import socket
import random
import argparse
#Making standart socket and trying to bind it with local ip and random port
old_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    try:
        old_socket.bind((socket.gethostbyname(socket.gethostname()), random.randint(1001, 65335)))
        break
    except:
        None
ip = argparse.ArgumentParser()
ip.add_argument("--ip",help = "Servers IP address to what you need to connect")
adress = ip.parse_args().ip
old_socket.connect((str(adress), 8000))
#Making new socket for future connection
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
random_port = 0
#Same way to binding as first socket
while 1:
    try:
        random_port = random.randint(1001, 65535)
        new_socket.bind((socket.gethostbyname(socket.gethostname()), random_port))
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
while 1:
    text = input(">")
    if text == "close":
        conn.send("close".encode("UTF-8"))
        conn.close()
        break
    conn.send(text.encode("UTF-8"))
    message = conn.recv(10240).decode("UTF-8")
    if message != "404":
      print(message)
    else:
      print("command doesn't found")