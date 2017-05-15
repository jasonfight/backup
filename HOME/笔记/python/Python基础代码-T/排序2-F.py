#!/usr/bin/python
#coding=utf-8

#将输入的数按照顺序排列后进行输出
#使用python的交换方式
a = input()
b = input()
c = input()

if a > b:
    a,b = b,a

if a > c:
    a,c = c,a

if b > c:
    b,c = c,b

print "a = %d,b = %d,c = %d"%(a,b,c)
