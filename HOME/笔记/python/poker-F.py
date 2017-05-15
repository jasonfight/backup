#!/usr/bin/python
#coding=utf-8
'''
将1到13的扑克牌发一张,然后往底下放一张,发完之后,桌上的顺序为1-13,还原未发牌前的扑克牌顺序

算法:
发牌时,发一张然后从上往下拿一张,直到最后一张,直接发,
还原时,从桌上拿一张,然后将手中的牌从下往上拿一张,知道最后一张,只从桌上拿一张
实现:将原队列中从后往前一次弹出,新队列使用头插法,接收原队列弹出的数,然后将队尾的数弹出,插入到队头
直到弹出原队列最后一张是,新队列值插入.结束

'''
from collections import deque
n=[1,2,3,4,5,6,7,8,9,10,11,12,13]
m=deque([])			

m.appendleft(n.pop())
while True:
    m.appendleft(n.pop())
    m.appendleft(m.pop())
    if n == [1]:
        m.appendleft(n[0])
        break
print m





'''
n=[1,2,3,4,5,6,7,8,9,10,11,12,13]
m=[]
m.insert(0,n.pop())
while True:
    m.insert(0,n.pop())
    m.insert(0,m.pop())
    if n == [1]:
        m.insert(0,n[0])
        break
print m
'''
