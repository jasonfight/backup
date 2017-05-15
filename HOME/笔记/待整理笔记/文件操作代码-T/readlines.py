#!/usr/bin/python
#coding=utf-8
'''
readlines()的使用方法:
以列表的形式,返回f的内容,每一行为一个元素
'''


f = open('test.html','r')

buf = f.readlines(1)

print "++++++++++++++++++++++++++++++++"
print buf
print "++++++++++++++++++++++++++++++++"
