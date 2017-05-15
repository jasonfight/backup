#!/usr/bin/python

import signal
import time

signal.alarm(5)

time.sleep(3)

num = signal.alarm(4)
print num
#signal.pause()

while True:
    time.sleep(1)
    print "wait....."
