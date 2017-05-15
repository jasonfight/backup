#!/usr/bin/python

from signal import *
import os,time

def receive_sig(signum,stack):
    if signum == SIGINT:
        print "keep...."
    elif signum == SIGALRM:
        print "receive a alarm"
        print stack
    else:
        print "other signal"



alarm(7)

signal(SIGINT,receive_sig)
signal(SIGALRM,receive_sig)

print "My PID is :",os.getpid()

while True:
    print "Waiting..."
    time.sleep(2)
