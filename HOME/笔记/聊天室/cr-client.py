#! /usr/bin/python
#coding=utf-8
from time import ctime,sleep
import threading
import traceback,os,sys,signal
from socket import *

def send(s):
    while True:
        try:
            data = raw_input('>')
            s.sendto(date,ADDR)
        except(KeyboardInterrupt,SystemExit):
            raise
            traceback.print_exc()
            s.close()
            sys.exit(0)
def recv(s):
    while True:
        try:
            data = s.recvfrom(BUFSIZE)
            print data
        except(KeyboardInterrupt,SystemExit):
            raise
            traceback.print_exc()
            s.close()
            sys.exit(0)




HOST = "10.1.1.130"
PORT = int(sys.argv[1])
BUFSIZE = 1024
ADDR = (HOST,PORT)
s = socket(AF_INET,SOCK_DGRAM,0)  # ====> socket()
name = raw_input('请输入姓名:')
s.sendto('*'+name,ADDR)


t1 = threading.Thread(target = send,args=(s,))
t2 = threading.Thread(target = recv,args=(s,))
t1.setDaemon(True)
t1.start()
t2.setDaemon(True)
t2.start()


t1.join()
t2.join()
s.close
