#!/usr/bin/python
#coding=utf-8
'''
zip() 函数的使用
'''
keys = ['spam','eggs','toast']
vals = [1,3,5]

d = {}

for (k,v) in zip(keys,vals):
    d[k] = v

print d
