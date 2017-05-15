#!/usr/bin/python
#coding=utf-8
from socket import *
import sys
from time import sleep
dest = ('<broadcast>',8888)
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
print 'Looking for replise; press Ctrl+C to stop'
while True:
    sleep(1)
    s.sendto('hello',dest)
    buf,addr = s.recvfrom(1024)
    if not len(buf):
        break
    print "Recevied from %s:%s"%(addr,buf)
