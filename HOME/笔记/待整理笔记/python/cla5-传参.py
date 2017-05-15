#!/usr/bin/python

class A():
    def fun(self,a):
        print a

class B(A):
    def fun(self,a,b):
        print a + b


b = B()

#b.fun(1)

b.fun(1,2)  # NOTE:  实例化的对象在调用类中的方法时,应按照严格按照方法的参数进行传参
