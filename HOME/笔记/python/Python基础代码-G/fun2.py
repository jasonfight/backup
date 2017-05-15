#!/usr/bin/python
#coding=utf-8
#地址传参:
def fun(a):
    a.append(5)
    print a
l = [1,2,3,4]
a = l[:]            # 将l与a分离开,a的改变对l不造成影响
#a=l
fun(a)
print l

#值传参:  参数在函数中的改变不影响参数本身
def fun1(a):
    a=a+1
    print a
a=1
fun1(a)
print a
