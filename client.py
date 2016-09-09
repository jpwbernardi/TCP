#!/usr/bin/python3
import socket
import sys

#./client.py <ipserver> <port> <orderFile>

if (len(sys.argv) != 4):
    print("Número errado de argumentos!")
    sys.exit();

serverID = sys.argv[1]; filepath = sys.argv[3];
try:
    port = int(sys.argv[2]);
    f = open(filepath, 'r')
except ValueError:
    print("Porta deve ser um inteiro!")
except:
    print("Não foi possível abrir o arquivo!")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (serverID, port)
print(">>{}".format(server_address))
print ("connecting to {} port {}".format(server_address, sock.connect(server_address)))
try:
    # Send data
    print ("sending message...")
    message = f.read()
    sock.sendall(bytes(message, 'utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(bytes(message, 'utf-8'))

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print ("received \"{}\"".format(data))

finally:
    print("closing socket")
    sock.close()
