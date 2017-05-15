#!/usr/bin/python
#coding=utf-8
from socket import *
from time import *
import sys

HOST = '10.1.1.130'
PORT = int(sys.argv[1])
ADDR = (HOST,PORT)
BUFERSIZE = 1024
sockfd = socket(AF_INET,SOCK_DGRAM,0)
sockfd.bind(ADDR)

while True:
    print '等待客户端发送消息中..'
    data,addr = sockfd.recvfrom(BUFERSIZE)
    print data
    print '============='
    sockfd.sendto(ctime(),addr)
sockfd.close()
