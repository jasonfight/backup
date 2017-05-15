#!/usr/bin/python
#coding=utf-8



def fun(a):
    a = a[:]		#将a的副本传递给参数中, 函数的操作不会改变a的值
    a[1] = 100
    print "fun:",a

l = [1,2,3,4,5]

print l			

print "+++++++++++++++++++"

fun(l)			#输出:[1.100.3.4.5]

print l			#输出:[1.2.3.4.5]
