#!/usr/bin/python
#coding=utf-8
from linklist2 import *

l=Linklist()
l.initlist([1,2,3,4,5])
l.show()
print l.getlength()
l.insert(1,10)
l.show()
print "------"
l.delete(4)
l.show()
