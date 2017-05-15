#!/usr/bin/python
#coding=utf-8
'''
if语句的嵌套
'''
a = input()

if a > 0:
    if a > 10:
        print "a > 10"
    else:
        print "0 < a <= 10"
elif a == 0:
    print "a = 0"
else:
    print "a < 0"
