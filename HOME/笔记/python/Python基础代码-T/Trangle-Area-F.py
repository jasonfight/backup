#!/usr/bin/python
#coding=utf-8
'''
#输入三角形三条边求面积
先判断两边之和是否大于第三边,符合条件,进行运算
运算公式为   s=(a+b+c)/2   面积为 s*(a+b)*(b+c)*(a+c) 在进行开方 
'''
import math

a = input()
b = input()
c = input()

if a + b < c or a + c < b or b + c < a:
    print "input error"
    exit()

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print "The area is %.2f"%area
