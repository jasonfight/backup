#!/usr/bin/python
#coding=utf-8!
from linklist import *

print "单链表的增删改查:"
print ""
l = Linklist()
l.initlist([1,2,3,4,5])


print "初始链表的值:"
l.show()
print "链表的长度:"
print l.getlength()

print "在下标为2的位置添加100后的链表的值:"
l.insert(2,100)
l.show()

print "删除值为5的结点:"
l.delete(5)
l.show()

print "列出值为100的结点的下标:"
print l.index(100)

print "列出下标为2的结点的值"
print l.getitem(2)

print "使用__getitem__魔法方法列出下标为4的结点的值:"
print 'l[4]=',l[4]

print "使用__setitem__魔法函数修改值"
l[4] = 40
l.show()
