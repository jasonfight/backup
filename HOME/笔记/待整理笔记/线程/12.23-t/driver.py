#!/usr/bin/python

import os
from signal import *

def salar(signo,stack):
    if signo == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    if signo == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    if signo == SIGUSR1:
        print "please get off the bus"
        exit()
def driver(signo,stack):
    if signo == SIGUSR1:
        print "let us gogogo!"
    if signo == SIGUSR2:
        print "stop the bus!"
    if signo == SIGTSTP:
        os.kill(pid,SIGUSR1)
        os.wait()
        exit()


pid = os.fork()

if pid < 0:
    print "fail to fork"
    exit()
elif pid == 0:
    signal(SIGINT,salar)
    signal(SIGQUIT,salar)
    signal(SIGUSR1,salar)
    signal(SIGTSTP,SIG_IGN)
else :
    signal(SIGUSR1,driver)
    signal(SIGUSR2,driver)
    signal(SIGTSTP,driver)
    signal(SIGINT,SIG_IGN)
    signal(SIGQUIT,SIG_IGN)

while True:
    pass


