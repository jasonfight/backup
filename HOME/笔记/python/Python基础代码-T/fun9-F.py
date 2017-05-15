#!/usr/bin/python
#coding=utf-8

def fun(x,*args,**kwargs):
    print x	#输出 1
    print args  #输出 (2,3,4)
    print kwargs #输出 {'a': 5, 'b': 6}

fun(1,2,3,4,a = 5,b = 6)
