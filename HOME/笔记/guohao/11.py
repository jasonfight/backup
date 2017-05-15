#!/usr/bin/python
#coding=utf-8
'''
11. 编写一个TCP多线程并发服务器
'''

import sys,os
from socket import *


host = ''
port = int(sys.argv[1])
sockfd=socket()
sockfd.bind((host,port))

while True:
    connfd,addr=sockfd.recv(1024) #
    pid = os.fork()
    print '链接成功...'
    connfd,addr=sockfd.recv(1024) #
    if pid < 0:
        print 'error'
        exit()
    if pid > 0 :
        connfd.close()
        continue
    if pid == 0:
        sockfd.close()
        data = connfd.recv(1024)
        print data
        sockfd.sendto(ctime(),addr)
sockfd.close()
