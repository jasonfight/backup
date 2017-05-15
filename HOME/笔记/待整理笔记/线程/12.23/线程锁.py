#!/usr/bin/python
#coding=utf-8

import threading
from time import sleep

a=b=0

def value():
    while True:
        lock.acquire()
        if a != 0:
            print 'a=%d,b=%d'%(a,b)
