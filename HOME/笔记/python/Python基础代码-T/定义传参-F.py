#!/usr/bin/python
#coding=utf-8

'''
定义参数时的参数设置

'''
#定义位置参数的函数
def fun(a,b):
    print a,b
fun(1,2)
#输出:1 2

#定义默认值传参
def fun1(a,b = 100,c = 1000):
    print a,b,c
fun1(1,2)
#输出:1 2 1000

#收集位置参数方式
def fun2(a ,*b):
    print a,b
fun2(1,2,3,4,5,6)
#输出: 1 (2, 3, 4, 5, 6)


#收集字典的方式
def fun3(a,**b):
    print a,b
fun3(1,c = 2,b = 3)
#输出: 1 {'c': 2, 'b': 3}


def fun4(a,d = 100,*b,**c):	#顺序:先位置传参,再默认值传参,然后收集位置传参,最后为收集字典传参
    print a,b,c,d
fun4(1,2,3,4,5,b = 6,c = 7)
#输出:1 (3, 4, 5) {'c': 7, 'b': 6} 2
















