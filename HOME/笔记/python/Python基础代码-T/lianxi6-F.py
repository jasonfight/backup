#!/usr/bin/python
#coding=utf-8

'''

从终端读入一个数,将整个列表向后移动n个位置
思路:将列表的最后一位的数插入到第一位中,输入n,循环n次
'''

def fun(l,n):
        
    while n != 0:
        l.insert(0,l[-1])
        del l[-1]
        n -= 1



while True:
    l = [1,2,3,4,5,6,7,8,9]
    #print l
    num = input("please input 1-9: ")
    if num < 1 or num > 9:
        print "input again!"
        continue
    fun(l,num)
    print l
