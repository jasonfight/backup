#!/usr/bin/python
#coding=utf-8
from multiprocessing import Process,Queue
import time

process_list = []

q = Queue()
def f(name):        # NOTE: 子进程代码,作用是每秒给队列中添加一项字符
    time.sleep(1)
    q.put(['hello'+str(name)])

if __name__ == "__main__":
    for i in range (10):
        p = Process(target = f,args = (i,)) # NOTE: 创建一个子进程,
        p.start()
        process_list.append(p)

    for j in process_list:
        j.join()

    for i in range(9):
        print q.get()[0]
