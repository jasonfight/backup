#!/usr/bin/python

from time import sleep
import os,sys

try:
    os.mkfifo('fifo1')
    os.mkfifo('fifo2')
except OSError:
    print "fifo exist"

r = open('fifo1','r+')
w = open('fifo2','r+')

while True:
    print r.readline()
    
    sys.stdout.flush()

    str = sys.stdin.readline()
    
    w.write(str)
    w.flush()
