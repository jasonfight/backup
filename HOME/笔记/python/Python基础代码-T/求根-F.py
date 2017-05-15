#!/usr/bin/python
#coding=utf-8

#求两个根
'''
求以 a b c 为系数的一元二次方程的根
思路:先判断b*b-4ac的值是否大于0,对其进行开方赋值给y,如果小于,则报错
然后根据 x=(-b±y)/2a

'''

import math

a = input("a:") # a : input
b = input("b:")
c = input("c:")

q = b * b - 4 * a * c

#判断输入出错
if q < 0:
    print "没有根"
    exit()

x = -b /(a * 2)
#   求开方
y = math.sqrt(q)   

x1 = x + y
x2 = x - y

print "x1:%.2f,x2:%.2f"%(x1,x2)
