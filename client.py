#!/usr/bin/python3
import socket
import sys

#No GUI: ./clent.py <ipserver> <port> <orderfile>

def processOrder(ip, port, path):
    #create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #answer that will be returned
    answer = bytes("", 'utf-8')

    try:
        #Connect the socket to the port where the server is listening
        server_address = (ip, port)
        sock.connect(server_address)
        f = open(path, 'r')
        message = f.read()
        bmessage = bytes(message, 'utf-8')
        bmessage = bytes(str(len(bmessage)) + '@', 'utf-8') + bmessage;
        sock.sendall(bmessage)
        #amount recv and amount expected
        amrcv = amexp = 0
        #Get the message lenght that will be received
        while True:
            answer += sock.recv(16)
            try:
                answer = answer.decode('utf-8').split('@')
                answer[1] = bytes(answer[1], 'utf-8')
                amexp = int(answer[0])
                amrcv = len(answer[1])
                answer = answer[1]
                break
            except:
                continue
        while amrcv < amexp:
            data = sock.recv(16)
            answer += data
            amrcv += len(data)
    except:
        answer = bytes("Unexpected error", 'utf-8')
    finally:
        sock.close()
        return answer.decode('utf-8');


def main(argv):
    if (len(sys.argv) != 4):
        print("Wrong number of arguments!")
        sys.exit()
    ipserver = argv[1]; filepath = argv[3];
    try:
        port = int(argv[2])
    except ValueError:
        print("Port must be an iteger!")
        sys.exit()
    except:
        print("Unexpected error!")
    print(processOrder(ipserver, port, filepath));

if __name__ == "__main__":
    main(sys.argv)
