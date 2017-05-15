#!/usr/bin/python
#coding=utf-8
'''
使用Queue队列的方式来进行进程间通信:

'''



from multiprocessing import Process,Queue

import time,os

process_list = []
q = Queue()

def f(name):    # NOTE: 子进程代码,作用是每秒给队列中添加一项字符
    time.sleep(1)
    q.put(['hello' + str(name)])    # NOTE: 给管道添加内容

if __name__ == '__main__':
    for i in range(10):
        p = Process(target = f,args = (i,)) # NOTE: 创建一个子进程,
        time.sleep(2)
        p.start()
        process_list.append(p)

    for j in process_list:  # NOTE: 将生成的10个进程进行阻塞操作,
        j.join()

    for i in range(10):     # NOTE: 从管道中读出内容,通常都从第一位置读出,
        print q.get()[0]
