#!/usr/bin/python
#coding=utf-8
'''
用于线程间通信,通过事件标示控制
为何一直循环??????/
'''
import threading
from time import sleep,ctime
e = threading.Event()

def wait_for_event():
    print "just wait..."
    ecent_is_set = e.wait()
    print 'event set1'

def wait_for_event_timeout(t):
    while not e.isSet():
        print 'wait for timeout'
        event_is_set = e.wait
        print "event set2"
        if event_is_set:
            print 'processing event'
        else:
            print 'doing other work'
t1 = threading.Thread(name = 'block',target = wait_for_event,args = ())
t1.start()
t2 = threading.Thread(name = 'nonblock',target = wait_for_event_timeout,args = (3,))
t2.start()

print 'waiting before call evevt.set()'

sleep(4)
e.set()
print 'event is set'
