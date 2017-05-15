#!/usr/bin/python
#coding=utf-8
'''
6. 编写一个空洞文件，大小为1K
'''
f = open('empty','w')
f.seek(1024,0)
f.write(' ')
