#!/usr/bin/python
#coding=utf-8
from socket import *
import traceback
host = ''
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind((host,port))
while True:
    try:
        message,address = s.recvfrom(1024)
        print  'Got data from:',address
        s.sendto ('I am here',address)
    except (KeyboardInterrupt,SystemExit):
        raise
        traceback.print_exc()
