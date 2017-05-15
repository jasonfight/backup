#!/usr/bin/python
#coding=utf-8

'''
思路:
1.先求出这个数的所有因子 yinzi
2,将所有银子相加得到result
3.如果result== i,输出 i
'''

a = 1000

for i in range(1,a):
    result=0
    for yinzi in  range(1,i):
        if i % yinzi == 0:
            result+=yinzi
    if i == result:
        print i
