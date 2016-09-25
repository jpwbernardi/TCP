#!/usr/bin/python3
import socket
import sys
import tkinter as tk
import threading
from tkinter import ttk
from _thread import *

#./server.py [<server> <port>]

def clientthread(conn, raddr, stop):
    message = bytes("", "utf-8");
    prod = set(); cost = 0; i = 0
    amount_received = 0
    amount_expected = 0
    firstmsg = bytes("", 'utf-8')

    while True:
        data = conn.recv(16)
        firstmsg += data
        try:
            firstmsg = firstmsg.decode('utf-8').split('@')
            message = bytes(firstmsg[1], 'utf-8')
            amount_expected = int(firstmsg[0])
            amount_received = len(message)
            break;
        except:
            continue;

    try:
        while amount_received < amount_expected:
            data = conn.recv(128)
            amount_received += len(data)
            message += data
            if (i == 0):
                print("{}: ({}/{})".format(raddr, amount_received, amount_expected))
            i = (i + 1) % 1000
            if (stop.is_set()):
                raise OSError()
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
    finally:
        conn.close()

def startserver(addr, port, thrd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (addr, port)
    print ("starting up on port {}".format(server_address))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(server_address)
    except:
        if thrd != None:
            thrd._done = True
        else: print("Port cannot be used");
        return
    sock.listen(10)

    try:
        stop = threading.Event()
        while thrd == None or not thrd.stopped():
            print ("waiting for a connection")
            connection, client_address = sock.accept()
            if (thrd != None and thrd.stopped()):
                stop.set()
                raise OSError('Server isn\'t running')
            print ("connection from {}".format(client_address))
            start_new_thread(clientthread, (connection, client_address, stop))
    except:
        print("Closing server...")
    finally:
        sock.close()
        if thrd != None:
            thrd._done = True

if __name__ == "__main__":
    port = 12123; server = 'localhost'
    if len(sys.argv) == 3:
        try:
            server = sys.argv[1];
            port = int(sys.argv[2])
        except:
            print("Port must be an integer")
    startserver(server, port, None)
