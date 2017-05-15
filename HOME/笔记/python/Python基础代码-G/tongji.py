#!/usr/bin/python
#coding=utf-8

#第一个位置传一个字母    第二个 串 字符串    返回    字符串当中 包含几个 字母
a = raw_input("请输入一个字符:")
if len(a) != 1:
    print "输入错误,请输入一个字符"
    exit()
b = raw_input("请输入一个单词:")
def fun(a,b):
    n = 0
    for i in b:
        if i == a:
            n += 1
    return n
s=fun(a,b)
print s
