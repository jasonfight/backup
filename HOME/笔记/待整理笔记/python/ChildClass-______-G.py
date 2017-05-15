#!/usr/bin/python
#coding=utf-8

'''
子类继承父类,但是子类中如果有和父类重合的属性,则在子类中会覆盖掉继承的属性.
输出结果:
Dad
Son
I have money
My dad have money

'''
class ParentClass(object):
    name = 'Dad'
    def func(self):
        print 'I have money'
class ChildClass(ParentClass):
    name = 'Son'
    def fun(self):
        print "My dad have money"
dad = ParentClass()
child = ChildClass()
print dad.name
print child.name
child.func()
child.fun()
