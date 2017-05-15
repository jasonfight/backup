#!/usr/bin/python

f = open('text.txt','r')

buf = f.read()
print buf

print "4444444444444444444"
a = open('text.txt','r')

buf1 = a.readline()
print buf1

print "222222222222222222"
b = open('text.txt','r')

buf2 = a.readlines()
print buf2
