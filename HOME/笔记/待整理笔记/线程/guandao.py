#!/usr/bin/python
#coding=utf-8

import sys,os
from time import sleep
'''
无名管道:通过在系统内存中建立一个管道,各个进程之间都可以
进行访问,达到进程间通信的目的
'''
(r,w) = os.pipe()  # NOTE:  创建一个无名管道,有读端和写端
pid = os.fork()
if pid <0 :
    print "fail to fork"
elif pid == 0:
    print "child...."
    os.close(w)
    r = os.fdopen(r)   # NOTE:  文件描述符重定向,取代原来的文件描述符  第二参数默认为"r"

    while True:
        buf = r.readline()
        print "buf:",buf
        sys.stdout.flush()
else:
    print "parent...."
    os.close(r)
    w = os.fdopen(w,'w')

    while True:
        buf = sys.stdin.readline()
        w.write(buf)
        w.flush()
