import threading
import socket
import random
import sqlite3
import os
#Just some random functions what can call
#Maked function to make new database
ip_list = list()
#_______________________ADMIN COMMANDS_START________________________
def disconnect(ip):
    return 1
def help_admin():
    return "help"
def show_ip():
    text1 = str()
    if len(ip_list) == 0:
        return "Nobody are connected at this moment"
    for i in ip_list:
        text1 = text1 + f"IP {i[0]}: {i[1]}\n"
    return text1

def host_ip():
  return socket.gethostbyname(socket.gethostname())
def admin_shell():
  admin_commands = {"ip_list": show_ip, "host_ip": host_ip}
  text_list = list()
  while 1:
    text = input("#").split()
    if admin_commands.get(str(text[0])) != None:
        if len(text) > 1:
              for i in range(1, len(text)):
                  text_list.append(text[i])
              print(admin_commands[text[0]](text_list))
        else:
            print(admin_commands[text[0]]())
    else:
          print("Command_doesn't founded")
#________________________ADMIN COMMANDS_CLOSE______________________
#________________________CLIENT_COMMANDS_START_____________________
def make_database(list1):
    if list1[0] in os.listdir(os.getcwd()):
        return f"Database '{list1[0]}' already created"
    sqlite = sqlite3.connect(list1[0])
    sqlite.close()
    return f"Database '{list1[0]}' created succesfully"
  
def hello_world():
  return "Hello world bitches"
def openprint():
  return "Hello world :)"

def closeprint():
  return "Goodbye cruel world:("

def helpcommand(args=None):
    file = open("help.help", "r")
    if args == None:
        commands = str(file.read())
        file.close()
        return commands
    else:
        text1 = file.read().split("\n")
        text = None
        for i in text1:
            if i.split(":")[0] == args[0]:
                return i
        return "Command doesn't founded"


#Command list with list of the commands as key and functions as value
command_list = {"open":openprint, "closeprint": closeprint, "create_db": make_database, "help": helpcommand, "hello":hello_world}
#Future command parser what working with command and argumments for functions

def command_parser(text):
    text_list = list()
    text = text.split()
    if command_list.get(str(text[0])) != None:
      if len(text) > 1:
        for i in range(1, len(text)):
            text_list.append(text[i])
        return  command_list[text[0]](text_list)
      else:
        return command_list[text[0]]()
    else:
      return None

#this is function for theard, that mean that it should work multiply times

def connection(conne,addr):
    log = open("log.txt", "a")
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
    ip_list.append(address)
#Close connecting with "old" socket, now server is ready to accept new connection
    conn.close()
#This variable show that function is already close connecting
    global x
    x = 1
#This part of code are command handler what take command from client and send answer back
    while 1:
      try:
        message = new_socket.recv(1024)
        try:
          if message != b'':
            log.write(f"{addr[0]}: {message.decode('UTF-8')}\n")
            result = command_parser(message.decode("UTF-8"))
            if message.decode("UTF-8") == "close":
                log.write(f"{addr[0]}: disconnected\n")
                ip_list.remove(address)
                new_socket.close()
                break
            if result !=None:
              new_socket.send(str(result).encode("UTF-8"))
            else:
              new_socket.send(str(404).encode("UTF-8"))
          else:
            log.write(f"{addr[0]}: disconnected\n")
            new_socket.close()
            ip_list.remove(address)
            log.close()
            break
        except:
          None
      except:
        log.write(f"{addr[0]}: disconnected\n")
        log.close()
        new_socket.close()
        ip_list.remove(address)
        break
    return None
#___________________________CLIENT_COMMANDS_CLOSE_____________
#Making socket and variable
x = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), 8000))
threading.Thread(target=admin_shell, args=()).start()
while 1:
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
