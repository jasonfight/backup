#!/usr/bin/python
#coding=utf-8
'''
输出一个字符在一个字符串中出现的次数
'''
def char(ch,char):
    n = len(char)
    i = 0
    num = 0

    while i < n:
        if char[i] == ch:	#出现一次,计数器加一
            num += 1
        i += 1

    return num

num = char('l',"hello world")
print num
