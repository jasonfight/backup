#!/usr/bin/python
#coding=utf-8
'''
2. 编写一个程序完成类似cp命令的文件复制工作
'''
import sys
f = open(sys.argv[1],'r')
cp = open(sys.argv[2],'w')

while True:
    str = f.readline(10)
    if str == '':
        break
    cp.write(str)

f.close()
cp.close()
