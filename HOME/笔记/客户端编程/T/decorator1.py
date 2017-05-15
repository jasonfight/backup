#!/usr/bin/python

def func(self):
    print "bar"

def decorator(cls):
    cls.bar = func
    return cls

@decorator   ###====> Foo = decorator(Foo)
class Foo():
    pass

foo = Foo()
foo.bar()
