#!/usr/bin/python
#coding=utf-8
'''
将test.html文件的前100个字节读取并赋值给bhf 并输出
'''

f = open('test.html','r')

buf = f.read(100)

print "++++++++++++++++++++++++++++++++"
print buf
print "++++++++++++++++++++++++++++++++"
