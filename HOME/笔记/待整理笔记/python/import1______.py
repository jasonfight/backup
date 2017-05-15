#!/usr/bin/python
#coding=utf-8
'''
执行结果:
1===============
you use getattr...
you use getattr...

['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
2===============

    This id a text

<class '__main__.A'>
1----------------
{}
2----------------
you use setattr...
3----------------
7
{'x': 7}
疑问点:
1.执行dir(a)时,为什么会将getattr魔法方法执行两遍
2.getattr魔法方法有啥用?
3.setattr魔法方法有啥用?


'''

class A(object):
    '''
    This id a text
    '''

    def __getattr__(self,name):
        print 'you use getattr...'
    def __setattr__(self,name,value):
        print 'you use setattr...'
        self.__dict__[name]=value

a=A()
print '1==============='
print dir(a)
print '2==============='
print a.__doc__
print a.__class__

a.x
print '1----------------'
print a.__dict__
print '2----------------'
a.x=7
print '3----------------'
print a.x
print a.__dict__
