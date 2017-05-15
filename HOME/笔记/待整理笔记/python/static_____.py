#!/usr/bin/python
#coding=utf-8

class TestStaticMethod:
#   @staticmethod      也可以用这种装饰器的方法声明这个方法为静态方法
    def foo():
        print("calling static method foo()")

    foo = staticmethod(foo)

class TestClassMethod:
    def foo(cls):
        print("calling class method foo()")
        print("class",cls.__name__)

    foo = classmethod(foo)

TestStaticMethod.foo()
TestClassMethod.foo()

A = TestStaticMethod()

A.foo()

B = TestClassMethod()
B.foo()

