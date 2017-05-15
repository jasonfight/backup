#!/usr/bin/python

from socket import *
from time import ctime
from select import *


HOST = "10.1.1.130"
PORT = 8882
BUFSIZE = 1024
ADDR = (HOST,PORT)


sockfd = socket(AF_INET,SOCK_STREAM,0)  # ====> socket()

sockfd.bind(ADDR)
sockfd.listen(5)
inputs = []

while True:

    rs,ws,es, = select(inputs,[],[])
    for r in rs:
        if r is sockfd:
            print 'Waiting for connection....'
            connfd,addr = sockfd.accept()
            print 'connected from:',addr
            inputs.append(connfd)
    else:
        try:
            data = r.recv(BUFSIZE)
            disconnect = not data
        except socket.error:
            disconnect = True
        if disconnect:
            print r.getperrname(),'disconnected'
            inputs.remove(r)
            r.close
        else:
            r.send('[%s]:%s)'%(ctime(),data))
