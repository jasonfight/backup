#!/usr/bin/python
#coding=utf-8

from time import sleep
import os,sys
try:
    os.mkfifo('fifo')
except OSError:
    print "fifo is exist"

f = open("fifo",'w+')
m = open('new','r+')

while True:
    str = sys.stdin.readline()
    f.write(str)
    f.flush()

    m = m.readline()
    print m
