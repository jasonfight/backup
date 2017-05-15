#!/usr/bin/python

import sys,os
from time import sleep 


(r,w) = os.pipe()


pid = os.fork()

if pid < 0:
    print "fail to fork"
elif pid == 0:		#子进程:读取
    print "child:"
    os.close(w)
    r = os.fdopen(r)
    
    while True:
        buf = r.readline()
        print "buf : ",buf
        sys.stdout.flush()
    
else:
    print "parent:"	#父进程:写入
    os.close(r)
    
    w = os.fdopen(w,'w')
    while True:
        buf = sys.stdin.readline()

        w.write(buf)
        w.flush()
