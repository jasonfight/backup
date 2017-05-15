#!/usr/bin/python
#coding=utf-8

'''
readline()函数的用法:
将test.html文件中第一行的10字节的内容输出
如果参数为空,则输出一行,带换行符


'''

f = open('test.html','r')
buf = f.readline(10)
buf2 = f.readline()

print "++++++++++++++++++++++++++++++++"
print buf
print buf2
print "++++++++++++++++++++++++++++++++"
