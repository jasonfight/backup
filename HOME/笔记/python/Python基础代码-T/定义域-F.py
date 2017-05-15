#!/usr/bin/python
#coding=utf-8

'''
全局变量和局部变量的作用域

全局变量为不可改变的值时,如果局部变量想要更改,则需要在局部变量前引入 global函数
同时,局部变量不能被外部函数使用
'''

def fun():
#    a = 3
#    b = 4
    global a
    a += 1
    print "in fun:",a,b
    num = 1000


a = 1
b = 2
fun()
print "out fun:",a,b
#print num
