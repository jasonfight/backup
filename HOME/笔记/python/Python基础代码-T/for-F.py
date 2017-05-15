#!/usr/bin/python
#coding=utf-8
'''
for 循环的使用
备注:使用for遍历字典,输出的是字典的键
'''

for i in [1,2,3,4,5]:
    print i,

print ""

for i in (1,2,3,4,5):
    print i,

print ""

for i in {1,2,3,4,5}:
    print i,

print ""

for i in "hello":
    print i,

print ""

d = {'a':1,'b':2,'c':3}

for i in d:
    print i,":",d[i],

print ""
