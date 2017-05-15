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

while True:
    data = raw_input('请输入:')
    sockfd.sendto(data,ADDR)
    if not data:
        break
    recvdata = sockfd.recvfrom(BUFERSIZE)
    print recvdata
sockfd.close()
