#!/usr/bin/python
#coding=utf-8

for i in range(3,20):
    #print i
    k=0
    for j in range(1,i):
        num=i%j
        if num==0:
            k+=1
    if k==1:
        print i
