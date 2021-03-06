#!/usr/bin/python 
#coding=utf-8
'''
递归函数的使用方法:
该题解决思路:

n=4 x=6

P(4,6)=(7*6*P(3,6)-3*P(2,6))/2 = 5483
P(3,6)=(5*6*P(2,6)-2*P(1,6))/2 = 526
P(2,6)=(3*6*P(1,6)-P(0,6))/2 = 53
P(1,6)=6
P(0,6)=1
将P的各个值代入公式,即可计算出P(4,6)的值为5483

'''

def P(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return x

    return ((2 * n - 1)*x*P(n - 1,x) - (n - 1)*P(n - 2,x)) / n

print P(3,6)

