#!/bin/python
#coding=utf-

'''
3. 编写一个程序，使用有名管道完成类似于两个终端对话的操作。
即每个终端输入内容对方可以收到，交替进行
'''
import os,sys

try:
    os.mkfifo('new')
    os.mkfifo('fifo')
except:
    print 'exist'

r = open('fifo','r')
w = open('new','w')

while True:
    print '待接收...:'
    print r.readline()
    sys.stdout.flush()
    print '待发送...:'
    buf = sys.stdin.readline()
    w.write(buf)
    w.flush()
