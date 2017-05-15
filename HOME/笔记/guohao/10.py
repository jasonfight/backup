#!/usr/bin/python
#coding=utf-8
'''
10 编写一个udp的循环服务器模型
'''
from socket import *
from time import *
import sys

HOST = ''
PORT = int(sys.argv[1])
ADDR = (HOST,PORT)
sockfd = socket(AF_INET,SOCK_DGRAM,0)
sockfd.bind(ADDR)

while True:
    print '等待客户端发送消息中..'
    data,addr = sockfd.recvfrom(1024)
    print data
    sockfd.sendto(ctime(),addr)
sockfd.close()
