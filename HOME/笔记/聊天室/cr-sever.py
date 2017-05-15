#!/usr/bin/python
#coding=utf-8
from socket import *
from time import *
import sys

def login():
    data,addr = sockfd.recvfrom(BUFERSIZE)
    b = {data:addr}
    a.update(b)
    print  data,'login'
    print a
def chat():
    # while True:
    data,addr = sockfd.recvfrom(BUFERSIZE)
    for i in a.keys():
        sockfd.sendto(ctime(),a[i])

HOST = '10.1.1.130'
PORT = int(sys.argv[1])
ADDR = (HOST,PORT)
BUFERSIZE = 1024
sockfd = socket(AF_INET,SOCK_DGRAM,0)
sockfd.bind(ADDR)

a = {}
print "server strat...."
while True:
    data,addr = sockfd.recvfrom(BUFERSIZE)
    if data[0] == '*':
        b = {data:addr}
        a.update(b)
        print a
        for i in a.keys():
            print 'i=:',i
            print 'a[%s]:%s'%(i[1:],a[i])
            sockfd.sendto('haha',a[i])
            print '--------------------'
sockfd.close()
