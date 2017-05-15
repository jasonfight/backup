#!/usr/bin/python
#coding=utf-8
__metaclass__ = type            # NOTE: 声明为新式类
class Person():

    print "This is a class"

    age = 10

    def __init__(self,name):
        self.name = name

    def color(self,color):
        print "%s is %s"%(self.name,color)

Lilei = Person('leilei')

print Lilei.age

print Lilei.name

Lilei.color('black')

print "****************************8"


Hanmei = Person('meimei')

print Hanmei.age

print Hanmei.name

Hanmei.color('yellow')
