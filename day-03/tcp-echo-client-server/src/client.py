import socket
import sys

ip="127.0.0.1"

remoteHost = "127.0.0.1"
remotePort = 50000

#create a socket
mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to remote host and port
mSocket.connect((remoteHost, remotePort))

print "connected to ", mSocket.getsockname()

#send request to host
msg = raw_input("Enter message: ")
mSocket.send(msg)

#get response
print "server response: "
receivedData = mSocket.recv(1024)
print "received: " + receivedData

mSocket.close()