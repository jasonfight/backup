#!/usr/bin/python
#coding=utf-8

'''
继承的用法
子类可继承父类的属性及方法
'''


class Animal(object):
    print "A new animal"	#加载类的时候执行该语句
    def call(self,yell):
        self.yell = yell

class Dog(Animal):
    color = 'yellow'
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

class Cat(Animal):
    color = "white"
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
wang = Dog()
miao = Cat()
wang.setName('dahuang')		# dahuang  有什么用?????
miao.setName('xiaomiao')

print wang.getName()
print miao.getName()
wang.call('wangwang')	#调用父类 Animal 的方法 yell
print wang.yell
miao.call('miaomiao')	#调用父类 Animal 的方法 yell
print miao.yell
