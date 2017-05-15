#! /usr/bin/python
#coding=utf-8

#将输入的数按照顺序排列后进行输出
#使用常规第三方数的方式

a = int(input())
b = int(input())
c = int(input())


if a > b:
    tmp = a
    a = b
    b = tmp

if a > c:
    tmp = a
    a = c
    c = tmp

if b > c:
    tmp = b
    b = c
    c = tmp

print("a = %d,b = %d,c = %d"%(a,b,c))
