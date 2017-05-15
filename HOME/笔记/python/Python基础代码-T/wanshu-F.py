#!/usr/bin/python
#coding=utf-8
'''
完数:
当一个数的所有因子之和等于自身时,该数成为完数
'''

for i in range(1,1001):
    num = 0
    for j in range (1,i / 2 + 1):
        if i % j == 0:
            num += j

    if num == i:
        print "%d "%num,

print ""
