#!/usr/bin/python
#coding=utf-8
#       求水仙花数,  即一个三位数的三位数的立方和为自身.
#for i in (100,102):
result=0
for i in range(100,1000):
    for
    num = i % 10
    i=i/10
    result=result+num**3

    if result==i:
        print i
