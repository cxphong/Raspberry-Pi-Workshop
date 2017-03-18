__author__ = 'akkaa_000'

import socket

#empty host string. bind() will use the current machine address
host = '127.0.0.1'
port = 50000
backlog = 5
size = 1024

#create a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#restart server quickly when it terminates. also to reuse the same port
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind the socket to a port
serverSocket.bind((host, port))

#listen for connections
serverSocket.listen(backlog)

print "server running on ", serverSocket.getsockname()
print "waiting for connections"

try:
    while 1:
        clientSocket, address = serverSocket.accept()
        print "connected from ", address

        while 1:
            receivedData = clientSocket.recv(size)

            if not receivedData:
                break

            print "data = ", receivedData
            clientSocket.send(receivedData)

        clientSocket.close()
        print "disconnected from ", address
finally:
    serverSocket.close()

