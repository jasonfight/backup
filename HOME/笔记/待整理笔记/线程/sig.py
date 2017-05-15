#!/usr/bin/python
#coding=utf-8
from signal import *
import time
'''
信号处理函数:
1.忽略信号
2.采用默认方式处理  默认处理方式:终止进程,暂停进程,忽略(不作任何处理)
3.采用指定函数处理

signal()函数:
signal([sianal,method])
参数一:需要处理的信号名称
参数二:处理方式
signal()函数为不阻塞函数,功能是向内核发送处理记录,用来后续查询.
'''
alarm(3)
signal(SIGALRM,SIG_DFL) # NOTE:   默认操作  DFL:default

signal(SIGALRM,SIG_IGN) ## NOTE: 忽略信号   ignore
while True:
    time.sleep(1)
    print "wait....."
