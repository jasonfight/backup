#!/usr/bin/python
#coding=utf-8

#杨辉三角

l = []

for i in range(10):
    l.append([])
    l[i].append(1)

    for j in range(1,i + 1):
        l[i].append(l[i - 1][j - 1] + l[i - 1][j])
    l[i].append(0)
    print l

for i in range(10):
    for j in range(i + 1):
        print "%5d"%l[i][j],
    print ""

