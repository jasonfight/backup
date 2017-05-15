#!/usr/bin/python
#coding=utf-8
'''
传参方式:
'''
def fun(a,b):
    print a,b


#位置传参
fun(1,2)
#输出: 1 2

#关键字传参
fun(1,b = 2)
#输出: 1 2

#*传参
l = [5,6]
fun(*l)
#输出: 5 6

#**传参
d = {"b":1,'a':3}
fun(**d)  #===>fun(b = 1,a = 3)
#输出: 3 1
