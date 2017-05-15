#!/usr/bin/python
#coding=utf-8
'''
lambda 匿名函数,一般可以看做是一个简单的表达式
语法:
函数名称=lambda 参数1,...,参数n:表达式

执行结果:
3
=============
4
8
16

'''

f=lambda x,y:x+y
print f(1,2)
print "============="

l=[ lambda x:x**2,
    lambda x:x**3,
    lambda x:x**4]
for i in l:
    print i(2)
