#!/usr/bin/python3
import socket
import sys
from _thread import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10002)
print ("starting up on port {}".format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

def clientthread(conn, raddr):
    message = bytes("", "utf-8");
    frase = "Uma frase deveras grande para obrigar a separar e enviar varios pacotes";
    amount_received = 0; i = 0
    amount_expected = 0 #int(sock.recv(16).decode('utf-8'))
    firstmsg = bytes("", 'utf-8')

    while True:
        data = conn.recv(16)
        firstmsg += data
        try:
            firstmsg = firstmsg.decode('utf-8').split('@')
            message = bytes(firstmsg[1], 'utf-8')
            #print(">>>{}".format(splitedstr))
            amount_expected = int(firstmsg[0])
            amount_received = len(message)
            break;
        except:
            continue;

    while amount_received < amount_expected:
        data = conn.recv(16)
        amount_received += len(data)
        message += data
        if (i == 0):
            print("{}: ({}/{})".format(raddr, amount_received, amount_expected))
        i = (i + 1) % 1000
    print("{}: ({}/{})".format(raddr, amount_received, amount_expected))
    print(message.decode('utf-8'))
    print ("No more data from {}".format(raddr))
    conn.sendall(bytes(str(len(bytes(frase, 'utf-8'))) + "@" + frase, 'utf-8'))
    conn.close()

try:
    while True:
        # Wait for a connection
        print ("waiting for a connection")
        connection, client_address = sock.accept()
        print ("connection from {}".format(client_address))
        start_new_thread(clientthread, (connection, client_address))
finally:
    sock.close()
