#!/usr/bin/python
#coding=utf-8
'''
使用Queue队列的方式来进行进程间通信:

'''
from multiprocessing import Process,Queue
import time,os

process_list = []

q = Queue()
def f(name):        # NOTE: 子进程代码,作用是每秒给队列中添加一项字符
    time.sleep(1)
    q.put(['hello'+str(name)])
    print os.getpid()

if __name__ == "__main__":
    for i in xrange (10):
        p = Process(target = f,args = (i,)) # NOTE: 创建一个子进程,
	time.sleep(0.1)        
	p.start()
        process_list.append(p)
        
    for j in process_list:
        j.join()

    for i in xrange(10):	#将队列中的内容提取出来
        print q.get()[0]
