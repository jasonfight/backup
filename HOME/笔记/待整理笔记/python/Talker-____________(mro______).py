#!/usr/bin/python
#coding=utf-8
'''
子类继承多个父类的继承顺序,
可通过mro函数来查看继承顺序
语法:
classname.mro()
'''


class Grandfather(object):
    name='yeye'
class Dad1(Grandfather):
    name = 'dad1'
#    pass
class Dad2(Grandfather):
    name = 'dad2'
class Kid(Dad1,Dad2):
    pass

a=Kid()
print Kid.mro()
print a.name
