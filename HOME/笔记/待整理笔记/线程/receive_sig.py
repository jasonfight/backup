#!/usr/bin/python
#coding=utf-8


'''
通过函数来处理信号:

'''
from signal import *
import os,time


def receive_sig(signum,stack):
    if signum == SIGINT :
        print "keep...."
    elif signum == SIGALRM :
        print "receive a alarm"
    else:
        print "other signal..."


alarm(3)                           # NOTE: 三秒后发送时钟信号
signal(SIGINT,receive_sig)      # NOTE: 捕捉到信号时,调用函数来处理信号
signal(SIGALRM,receive_sig)

print "My PID is :",os.getpid()

while True:
    time.sleep(1)
    print "waiting....."
