#!/usr/bin/python
#coding=utf-8
'''
return 的用法:
结束函数,并返回return后面的值,
如果为多个值,则返回一个元组
如果为计算式,则返回计算结果
输出结果:

hello world!
(1, 2, 3, 4)

3

'''
def fun():
    print "hello world!"
    return 1,2,3,4
    print "hello kitty!"

def fun1(a,b):
    return a + b


r = fun()
print r
print fun1(1,2)
