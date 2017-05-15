#!/usr/bin/python

from time import sleep
import os,sys

try:
    os.mkfifo('fifo1')
    os.mkfifo('fifo2')
except OSError:
    print "fifo exist"


w = open('fifo1','r+')
r = open('fifo2','r+')

while True:
    str = sys.stdin.readline()
    w.write(str)
    w.flush()

    print r.readline()
    sys.stdout.flush()
