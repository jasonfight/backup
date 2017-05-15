#!/usr/bin/python
#coding=utf-8
'''
函数的定义与调用

执行结果:
hello world!
++++++++++++++++
hello world!
++++++++++++++++
<type 'function'>

'''
def func():		#定义函数
    print "hello world!"
    print "++++++++++++++++"

func()			#调用函数

f = func		#将函数名赋值给一个变量

f()			#通过变量来调用函数
print type(f)		#检测f的类型 为<type 'function'>
