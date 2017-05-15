#!/usr/bin/python
# coding=utf-8
'''
写一个复制文件的程序:
'''
import sys

f = open(sys.argv[1],'r')      # NOTE: 以只读方式打开文件1
f_cp = open(sys.argv[2],'a') # NOTE: 以重写方式创建并打开文件2

while True:
    str = f.readline(10)      # NOTE: 将f中的每10个字节大小的内容,赋值给str
    if str == '':               # NOTE: 如果str为空,即读到f的末尾,停止循环
        break
    f_cp.write(str)           # NOTE: 将str中的内容写入f_cp中

f.close()
f_cp.close()
