#!/usr/bin/python
#coding=utf-8

class ParentClass():
    name = "老张"

    def func(self):
        print "老子有钱"

class ChildClass(ParentClass):
    name = "小张"
    def fun(self):
        print "哥也有钱"


child = ChildClass()

print child.name        # NOTE:  输出 小张, 子类与父类属性名相同,会覆盖父类
child.func()
child.fun()

parent = ParentClass()

parent.func()
