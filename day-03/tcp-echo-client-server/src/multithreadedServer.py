#!/usr/bin/env python
"""
Multi-threaded TCP Server

multithreadedServer.py acts as a standard TCP server, with multi-threaded integration, spawning a new thread for each
client request it receives.

This is derived from an assignment for the Distributed Systems class at Bennington College
"""

from argparse import ArgumentParser
from threading import Lock, Thread
from socket import SO_REUSEADDR, SOCK_STREAM, socket, SOL_SOCKET, AF_INET

#---------------------------------------#
########## USER INPUT HANDLING ##########
#---------------------------------------#

host="127.0.0.1"
port=50000

# -------------------------------------------#
########## DEFINE GLOBAL VARIABLES ##########
#-------------------------------------------#

counter = 0
response_message = "Now serving, number: "
thread_lock = Lock()

# Create a server TCP socket and allow address re-use
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((host, port))

# Create a list in which threads will be stored in order to be joined later
threads = []

#---------------------------------------------------------#
########## THREADED CLIENT HANDLER CONSTRUCTION ###########
#---------------------------------------------------------#


class ClientHandler(Thread):
    def __init__(self, address, port, socket, response_message, lock):
        Thread.__init__(self)
        self.address = address
        self.port = port
        self.socket = socket
        self.response_message = response_message
        self.lock = lock

    # Define the actions the thread will execute when called.
    def run(self):
        global counter
	while 1:
    	    data = self.socket.recv(1024)
	    if not data: break
	    print data
   	    self.socket.send(data)
        
	    # Lock the changing of the shared counter value to prevent erratic multithread changing behavior
            with self.lock:
               counter += 1

	print "close socket"
	self.socket.close()

#-----------------------------------------------#
########## MAIN-THREAD SERVER INSTANCE ##########
#-----------------------------------------------#

# Continuously listen for a client request and spawn a new thread to handle every request
while 1:

    try:
        # Listen for a request
        s.listen(1)
        # Accept the request
        sock, addr = s.accept()
        # Spawn a new thread for the given request

        print "connected from ", addr

        
        newThread = ClientHandler(addr[0], addr[1], sock, response_message, thread_lock)
        newThread.start()
        threads.append(newThread)
    except KeyboardInterrupt:
        print "\nExiting Server\n"
        break

# When server ends gracefully (through user keyboard interrupt), wait until remaining threads finish
for item in threads:
    item.join()
