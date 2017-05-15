#!/usr/bin/python
#coding=utf-8
#指定前两个数字,之后的每一个数为前两个数之和;

i=input("请输入第一个数:")
j=input("请输入第二个数:")
list=[i,j]
print list
print list[0]

for n in range(1,10):
    list.append(list[n-1]+list[n])
print list
