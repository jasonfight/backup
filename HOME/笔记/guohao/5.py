#!/usr/bin/python
#coding=utf-8
'''
5. 完成一个程序，在命令行直接输入一个文件目录，
打印出这个目录下的所有普通文件文件名。
'''
import sys,os

dir_name =sys.argv[1]
all_file =os.listdir('.')
# print all_file
for i in all_file:
    if os.path.isfile(i):
        print i,
print ''
