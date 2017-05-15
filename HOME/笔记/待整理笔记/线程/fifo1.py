#!/usr/bin/python
#coding=utf-8
'''
不对,带改正
'''
from time import sleep
import os,sys
try:
    os.mkfifo('new')
except OSError:
    print "new is exist"

m = open('new','w+')
f = open("fifo","r+")

while True:
    str = sys.stdin.readline()
    m.write(str)
    m.flush()

    a = f.readline()
    print a
