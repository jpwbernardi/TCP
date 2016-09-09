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
    answer = bytes("", 'utf-8')
    bmessage = bytes(message, 'utf-8')
    sock.sendall(bytes(str(len(bmessage)) + "@" + message, 'utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = 0 #int(sock.recv(16).decode('utf-8'))
    splitedstr = ""

    while True:
        data = sock.recv(16)
        print ("resposta \"{}\"".format(answer))
        answer += data
        print("Hm...");
        try:
            splitedstr = answer.decode('utf-8').split('@')
            splitedstr[1] = bytes(splitedstr[1], 'utf-8')
            print(">>>{}".format(splitedstr))
            amount_expected = int(splitedstr[0])
            amount_received = len(splitedstr[1])
            break;
        except:
            continue;
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        splitedstr[1] += data;
        print ("received \"{}\"".format(data))
    print(splitedstr)
finally:
    print("closing socket")
    sock.close()
