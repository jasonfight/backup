#!/usr/bin/python
#coding=utf-8


#输入一串数字型字符串,转换为数字

string=raw_input("请输入一串数字型字符:")
print type(string)
l=[]
result=0
for n in string:
    l.append(n)

for m in l:
    result=result*10+int(m)
print "result=",result
print type(result)
