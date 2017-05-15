#!/usr/bin/python
#coding=utf-8

l=input("请输入一个列表:")
l_ji=[]
l_ou=[]
for i in l:
    if i % 2 != 0:
        l_ji.append(i)
    else:
        l_ou.append(i)
for j in l_ou:
    l_ji.append(j)
print "before:",l
print "after:",l_ji
