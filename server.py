#!/usr/bin/python3
import socket
import sys
from _thread import *

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10003)
print ("starting up on port {}".format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

def clientthread(conn):
    message = bytes("", "utf-8");
    while True:
        data = conn.recv(16)
        message = message + data
        if data:
            print ("sending data back to the client")
            conn.sendall(data)
        else:
            print ("no more data from {}".format(client_address))
            conn.sendall(bytes(":)", "utf-8"))
            break
    conn.close()

try:
    while True:
        # Wait for a connection
        print ("waiting for a connection")
        connection, client_address = sock.accept()
        print ("connection from {}".format(client_address))
        start_new_thread(clientthread, (connection,))
finally:
    sock.close()
