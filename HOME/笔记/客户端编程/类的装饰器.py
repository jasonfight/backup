#!/usr/bin/python
#coding=utf-8
'''
需要掌握
'''
def func(a):
    print 'bar'
def decorator(cls):
    cls.bar = func
    return cls

@decorator #----->Foo = decorator(Foo)
class Foo():
    pass
foo = Foo()
foo.bar()
