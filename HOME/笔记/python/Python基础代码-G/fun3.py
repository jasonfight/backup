#!/usr/bin/python
#coding=utf-8
#定义函数时:

#1.位置传参
def fun(a,b):
    print a,b
fun(1,2)

#2.默认值传参
def fun1(a,b=100):
    print a,b
fun1(2,1)

#3.收集位置参数方式
def fun2(*a):
    print a
fun2(1,2,3)

#4.收集字典方式
def fun3(**a):
    print a
fun3(a=1,b=2,c=3)


#5.几种方式同时出现时的位置书写规范

def fun4(a,b=100,*c,**d):   #位置传参-->默认值传参-->收集位置传参-->收集字典传参
    print a,b,c,d
fun4(1,2,4,5,6,n=1,d=2,m=3)

#python3 中的不同:
def fun5(*a,b):
    print (a.b)
fun5(1,2,3,4,b=100)     # 可以将*a 放在前面, 但是调用是,要将声明b的值
