#! /usr/bin/python

from time import ctime,sleep
import threading
import traceback,os,sys,signal
from socket import *

def xiancheng(c):

    while True:
        print 'child from %s being hanled PID is %d'%(c.getpeername(),os.getpid())
        try:
            data = c.recv(BUFSIZE)
            print data
            c.send('recv you massage')
        except(KeyboardInterrupt,SystemExit):
            raise
            traceback.print_exc()
            c.close()
            sys.exit(0)



HOST = "10.1.1.130"
PORT = 8863
BUFSIZE = 1024
ADDR = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM,0)  # ====> socket()
s.bind(ADDR)
s.listen(5)

threads = []
while True:
    c,addr = s.accept()
    t = threading.Thread(target = xiancheng,args = (c,))
    t.setDaemon(True)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
s.close
