#!/usr/bin/python
#coding=utf-8


#调用函数时:


def fun(a,b):
    print a,b
#1.位置传参
fun(1,2)
#2.关键字传参
fun(b=1,a=2)        #

#3. *传参:
l=[5,6]
fun(*l)

#4.**传参
d={'a':1,'b':2}
fun(**d)     #--> fun(a=1,b=2)
