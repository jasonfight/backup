#!/usr/bin/python
#coding=utf-8
'''
题目要求：编程读写一个文件

，每隔1秒向文件中写入一行数据，类似这样：

1,  2016-12-20 19:57:00
2,  2016-12-20 19:57:01
该程序应该无限循环，直到按 Ctrl+C 中断程序。再次启动程序写文件时可以追加到原文件之后，
并且序号能够接续上次的序号，比如：
1,  2016-12-20 19:57:00
2,  2016-12-20 19:57:01
3,  2016-12-20 19:57:30
4,  2016-12-20 19:57:31
5,  2016-12-20 19:57:32
6,  2016-12-20 19:57:33
'''

import time
line = 0                        # NOTE: 计数器初始化

try:
    f = open('time.txt','a+')   # NOTE: 以读写并可追加模式打开文件
except IOError,e:               # NOTE: 如果打开文件错误,捕捉该错误并输出错误信息
    print e

for i in f:                     # NOTE: 每写入一行,计数器加1
    line += 1

while True:
    m = time.localtime()       # NOTE: 得到时间元组并赋值给m

    line += 1
    print >> f,'nihao'
    print >>f,"%d, %4d-%02d-%02d %02d:%02d:%02d"%(line,m.tm_year,m.tm_mon,\
    m.tm_mday,m.tm_hour,m.tm_min,m.tm_sec)    # NOTE: 将 需要打印的内容,写入f中
    f.flush()                                  # NOTE: 刷新缓冲区

    time.sleep(1)
