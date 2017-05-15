#!/usr/bin/python
#coding=utf-8

import sys
a=sys.argv[1]
f = open(a,'r')

buf = f.read()
print buf
print "........."

print open(sys.argv[1],'r').read()
