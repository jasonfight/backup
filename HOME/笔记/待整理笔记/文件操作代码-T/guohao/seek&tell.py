#!/usr/bin/python
#coding=utf-8

f = open('text.txt','r+')
f.seek(2)
f.write('hao')
print f.tell()
