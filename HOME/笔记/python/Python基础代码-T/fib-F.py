#!/usr/bin/python
#coding=utf-8
'''
斐波那契数列
从第三个数开始,每个数都是前面两个数只和

'''


l = [1,1]

for i in range(10):
    num = l[i] + l[i+1]
    l.append(num)

print l
