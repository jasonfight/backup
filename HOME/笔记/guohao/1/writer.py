#!/bin/python
#coding=utf-8
'''
1. 编写程序实现如下功能：

reader.py 从argv[1]所指定的文件中读取内容，依次写到管道 /home/linux/myfifo中

writer.py 从管道/home/linux/myfifo中读取内容，写到argv[1]所指定 的文件中并保存

代码中可省略模块引入，/home/linux/myfifo无需创建
'''


import os,sys
file_name = sys.argv[1]
w = open(file_name,'w')
r = open('myfifo','r')

while True:

    buf = r.readline()
    if buf != '':

        sys.stdout.flush()
        print buf
        w.write(buf)
    else:
        break
