#!/usr/bin/python3
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print ("connecting to {} port {}".format(server_address, sock.connect(server_address)))
try:
    # Send data
    message = 'Esse é um teste cheio de baboseira só para ser uma frase enormemente enorme e ver se ainda funciona tudo como deveria. Beijos de luz ;*';
    print ("sending \"{}\"".format(message))
    sock.sendall(bytes(message, 'utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ("received \"{}\"".format(data.decode('utf-8')))

finally:
    print("closing socket")
    sock.close()
