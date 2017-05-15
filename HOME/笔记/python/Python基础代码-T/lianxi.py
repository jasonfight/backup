#!/usr/bin/python
#coding=utf-8
'''
将终端输入的字符串去掉空格后输出
思路:
将字符使用split()函数 用空格进行分割,然后再用join函数使用空字符拼接到一起
'''
def fun(char):
    l = char.split(" ")
    char = ''.join(l)
    return char

while True:
    s = raw_input()
    if not len(s):
        break

    print "before:",s

    s = fun(s)
    print "after:",s
