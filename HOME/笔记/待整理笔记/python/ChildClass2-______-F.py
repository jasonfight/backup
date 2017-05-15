#!/usr/bin/python
#coding=utf-8
'''
多个子类继承父类:
输出结果:
centrary park
happiness
I can play basketball
I can play football
I can sleep
centrary park
happiness
I have money
'''
class ParentClass(object):
    name = 'Dad'
    add = 'centrary park'
    housename = 'happiness'
    def __init__(self,name):
        self.name=name
    def funP(self):
        print 'I have money'

class Child1(ParentClass):
    name = 'Son1'
    skill = 'baskball'
    def fun1(self):
        print "I can play basketball"

class Child2(ParentClass):
    name = 'Son2'
    skill = 'football'
    def fun2(self):
        print "I can play football"

class Child3(ParentClass):
    name = 'song3'
    skill = 'sleep'
    def fun3(self):
        print "I can sleep"
class Pet(Child3,ParentClass):
    pass

child1 = Child1('kobe')
child2 = Child2('C')
child3 = Child3('feiwu')
mary = Pet('mary')
print child1.add
print child2.housename
child1.fun1()
child2.fun2()
child3.fun3()
print mary.add
print mary.housename
child1.funP()
