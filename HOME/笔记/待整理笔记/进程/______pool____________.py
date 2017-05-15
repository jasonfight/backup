#!/usr/bin/python
#coding=utf-8

''' 
使用 multiprocessing 模块中的 pool 类来创建进程

'''
from multiprocessing import Pool
import os,time,random


def a(name):
    print "开始运行"
    time.sleep(2)
    print "子进程%s正在运行"%name
    print "运行结束"
    print '-------'



if __name__ == '__main__':
    print "父进程pid: ",os.getpid()
    p = Pool(4)				#使用多核进行多任务编程

    for i in range(16):
	#time.sleep(1)
        p.apply_async(a,args = (i,))
    p.close()
    p.join()

    print "All processs end"

