#!/usr/bin/python
#coding=utf-8
'''
9. 编写python程序: 编写一个函数addrs ，可以接收任意多个参数，
求这些参数的和。参数之和可以为数字相加，也可以是字符串的拼接。
但是如果类型不对无法进行加法操作是能够捕获到这个异常并且做出提示。

思路:
1.


'''
def addrs(a):
    x=type(a[0])
    if x == int:
        try:
            result=0
            for i in a:
                type(i)==int
                result+=i
            print "所有数字之和为:",result
        except TypeError:
                print "数字不能和字符相加"
    if x == str:
        try:
            result=""
            for i in a:
                type(i)==str
                result+=i
            print '所有字符串相连接为:',result
        except TypeError :
            print "字符不能和数字相加"
a=input("input nums or strs:")
addrs(a)
