#!/usr/bin/python

import os,time
from signal import *

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid == 0:
    time.sleep(0.1)
    print "This is child process",os.getpid()
    print os.getppid()
    exit('hahahha')

else:
    signal(SIGCHLD,SIG_IGN)
    print "This is parent process",os.getpid()
    print pid
    while True:
        pass

print "+++++++++++++++++++"
