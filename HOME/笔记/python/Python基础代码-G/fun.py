#!/usr/bin/python
#coding=utf-8

def function(): #函数的声明,括号里为形参,可不加self.
    print "nihao"
print "22222222222"
function()  #调用,括号里为实参,与形参对应,
z=function   #函数可看做为变量,可以通过赋值来更改其函数名,该变量为函数型变量
z()
print type(z)
