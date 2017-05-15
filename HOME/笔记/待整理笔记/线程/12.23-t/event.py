#!/usr/bin/python
#coding=utf-8

#用于线程间通信 通过事件标识控制

import threading
from time import sleep,ctime

e = threading.Event()
def wait_for_event():
    '''wait for the event to be set before doing anything'''
    print('wait for event starting')
    event_is_set = e.wait()
    print('event set1:%s'%event_is_set)

def wait_for_event_timeout(t):
    '''wait t seconds and then timeout'''
    while not e.isSet():
        print('wait for event timeout starting')
        event_is_set = e.wait(t)
        print('event set2:%s'%event_is_set)
        if event_is_set:
            print('processing event')
        else:
            print('doing other work')

t1 = threading.Thread(name = 'block',target = wait_for_event,args = ())
t1.start()
t2 = threading.Thread(name = 'nonblock',target = wait_for_event_timeout,args =
        (3,))
t2.start()

print('waiting before calling event.set()')
sleep(4)
e.set()
print('event is set')

