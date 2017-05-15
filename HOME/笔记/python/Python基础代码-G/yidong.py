#!/usr/bin/python
#coding=utf-8
#从终端读取一个1-9的数,将列表[1,2,3,4,5,6,7,8,9]的所有元素向后移动几位.

l=[1,2,3,4,5,6,7,8,9]
i=input("请输入1-9中的任意一个整数:")
if i not in l:
    print "输入错误"
    exit()

print
