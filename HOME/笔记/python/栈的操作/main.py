#!/usr/bin/python
#coding=utf-8
from stack import *
print "栈的增加和删除:"
print ""
s = Stack()
s.initstack([1,2,3,4,5])

print "初始栈的值:"
s.show()

print "栈顶增加一个值为10的结点:"
s.head_append(10)
s.show()

print "栈顶删除一个结点:"
s.pop()
s.show()

print "栈的长度:"
print s.getlength()

print "列出值为3的结点的下标:"
print s.index(3)

print "列出下标为4的结点的值:"
print s.getitem(4)

print "使用__getitem__魔法方法列出下标为4的结点的值:"
print 's[4]=',s[4]
