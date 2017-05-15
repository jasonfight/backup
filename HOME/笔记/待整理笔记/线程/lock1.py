#!/usr/bin/python

import threading
from time import sleep

a = b = 0

def value():
    while True:
        lock.acquire()
        if a != b:
            print('a = %d,b = %d'%(a,b))
        lock.release()

lock = threading.Lock()
t = threading.Thread(target = value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

