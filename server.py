#!/usr/bin/python3
import socket
import sys
from _thread import *

def clientthread(conn, raddr):
    message = bytes("", "utf-8");
    prod = set(); cost = 0;
    amount_received = 0; i = 0
    amount_expected = 0
    firstmsg = bytes("", 'utf-8')

    while True:
        data = conn.recv(1024)
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
    print ("No more data from {}".format(raddr))
    message = message.decode('utf-8').split('\n')
    for m in message:
        if (len(m) < 2): break;
        m = m.replace(")", "");
        m = m.split(",");
        prod.add(m[0]);
        cost += int(m[1]) * float(m[2]);
    frase = "O pedido contém {} itens e resulta em um valor total de R$ {:.2f}.".format(len(prod), cost);
    conn.sendall(bytes(str(len(bytes(frase, 'utf-8'))) + "@" + frase, 'utf-8'))
    conn.close()

def startserver(addr, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = (addr, port)
    print ("starting up on port {}".format(server_address))
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(10)

    try:
        while True:
            # Wait for a connection
            print ("waiting for a connection")
            connection, client_address = sock.accept()
            print ("connection from {}".format(client_address))
            start_new_thread(clientthread, (connection, client_address))
    finally:
        sock.close()

if __name__ == "__main__":
    startserver('localhost', 10007)
