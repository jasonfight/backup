#!/usr/bin/python
#coding=utf-8
import math
a=input("please input a:")
b=input("please input b:")
c=input("please input c:")
d=b**2-4*a*c
if d<0:
    exit()
s=math.sqrt(d)
x1=(-b+s)/2/a
x2=(-b-s)/2/a
print "第一个解为",x1
print "第二个解为",x2
