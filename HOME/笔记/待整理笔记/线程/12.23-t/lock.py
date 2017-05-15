#!/usr/bin/python
#coding=utf-8

#使用线程锁

import random
import threading
from time import sleep

class Counter:
    def __init__(self,start = 0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        print('waiting for lock')
        self.lock.acquire()
        try:
            print('Acquire lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        print('Sleeping %0.02f'%pause)
        sleep(pause)
        c.increment()
    print('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target = worker,args = (counter,))
    t.start()

print('waiting for worker threads')
main_thread = threading.currentThread() # 返回当前线程对象

for i in threading.enumerate():  #返回当前活动线程列表
    if t is not main_thread:
        t.join()
print('counter :%d'%counter.value)
