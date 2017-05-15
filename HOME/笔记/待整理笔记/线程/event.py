#!/usr/bin/python
#coding=utf-8
#用于线程间通信 通过事件标识控制

import threading
from time import sleep,ctime

def wait_for_event(e):
    '''在事件被设置之前,一直等待'''
    print('等待事件开始')

    event_is_set = e.wait()	#事件没有被设置前,一直阻塞
    print('事件set1:%s'%event_is_set)

def wait_for_event_timeout(e,t):
    '''等待一段时间后,进行超时操作'''
    while not e.isSet():
        print('等待超时中')
        event_is_set = e.wait(t)  #等待t秒后,冲破阻塞
        print('事件set2:%s'%event_is_set)
        if event_is_set:
            print('事件被设置')
        else:
            print('事件未被设置')


e = threading.Event()

t1 = threading.Thread(name = 'block',target = wait_for_event,args = (e,))
t1.start()

t2 = threading.Thread(name = 'nonblock',target = wait_for_event_timeout,args = (e,2))
t2.start()

print('10秒后事件将被设置')
sleep(11)
e.set()
print('事件被设置')

