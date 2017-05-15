#!/usr/bin/python
# coding=utf-8
'''
写一个类似shell中 cat 命令的程序
'''
import sys

try:
    f = open(sys.argv[1],'r')               
    buf = f.read()          # NOTE: 读取f中的所有内容,赋值给buf
except IOError as e:  # NOTE: 如果参数输入错误,则被该语句捕捉,执行该语句
    print e         # NOTE:  打印e的默认语句,如果print 后gender字符串,则输出该字符串
else:
    print buf
