#!/usr/bin/python
#coding=utf-8
'''
为避免忘记关闭流,可使用with语句来自动打开并关闭,确点是在with外,不能进行read()等操作
'''

with open('test.txt','r+') as f:
    str = f.read()

print str           # NOTE: 打印str

print f.read()      # NOTE: 报错!!!
