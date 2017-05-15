#!/usr/bin/python
#coding=utf-8
a=[1,1]
for i in range(1,19):
    print 'a[%d]='%i,a[i-1]
    a.append(a[i-1]+a[i])
print a
