#!usr/bin/python
#coding=utf-8
#从终端输入三个数,按照从小到大方式输出.


a=input("please input num1:")
b=input("please input num2:")
c=input("please input num3:")

if a>b:
    a^=b;b^=a;a^=b  #或者a,b=b,a 或是:tmp=a;a=b;b=tmp
if a>c:
    a^=c;c^=a;a^=c
if b>c:
    b^=c;c^=b;b^=c
print "a=%d,b=%D,c=%d"%(a,b,c)
