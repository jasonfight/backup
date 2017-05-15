#!/usr/bin/python
#coding=utf-8


import sys

f = open('test.txt','r+')


str = f.write("hello")      # NOTE: write函数的返回值是None,
print '1.......:',str

print '2.......',f.tell()     # NOTE: 打印指针位置 ,为5

f.seek(5,1)                 # NOTE: 以当前位置,将指针向后移动5位

str = f.read(5)              # NOTE: 读取5字节的内容赋值给str
print '3.......:',str

print '4........:',f.tell()     # NOTE: 打印指针位置
