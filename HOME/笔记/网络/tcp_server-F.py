#!/usr/bin/python

from socket import *
from time import ctime


HOST = "10.1.1.130"
PORT = 8884
BUFSIZE = 1024
ADDR = (HOST,PORT)


sockfd = socket(AF_INET,SOCK_STREAM,0)  # ====> socket()

sockfd.bind(ADDR)

sockfd.listen(5)

while True:	
    print 'Waiting for connection....'
    sockfd.setblocking(True)
    connfd,addr = sockfd.accept()
    print "++++++++"
    print 'connected from:',addr
    

    while True:
        data = connfd.recv(BUFSIZE)
        if data == '\r\n':
            break
        print data
        connfd.sendall('[%s]\n'%ctime())

connfd.close()
sockfd.close()
