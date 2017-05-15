#!/usr/bin/python
#coding=utf-8

from socket import *
import traceback,os,sys,signal



HOST = "10.1.1.130"
PORT = 8870
BUFSIZE = 1024
ADDR = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM,0)  # ====> socket()
s.bind(ADDR)
s.listen(5)

while True:
    try :
        c,addr = s.accept()
    except KeyboadInterrupt:
        raise
        traceback.print_exc()
    signal.signal(SIGCHILD,SIG_IGN)   # NOTE: 使用信号忽略的方式,防止僵尸进程


    pid = os.fork()
    if pid > 0:
        c.close()
        continue
    if pid == 0:
        s.close()
        try:
            print 'child from %s being hanled PID is %d'%(c.getpeername(),os.getpid())
            while True:
                data = c.recv(BUFSIZE)
                if not len(data):
                    break
                print data
                c.send('recv you massage')
        except(KeyboardInterrupt,SystemExit):
            raise
            traceback.print_exc()
            c.close()
            sys.exit(0)
