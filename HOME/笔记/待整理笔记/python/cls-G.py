#!/usr/bin/python
#coding=utf-8
class Person():                                 #声明一个类,约定类的第一个字母大写
    age = 10
    name = "Lilei"

    def color(self,color):                      #自带一个参数,用来传递对象的名称
        print "%s is %s"%(self.name,color)

#age = 20

#print age

Lilei = Person()                #实例化一个对象

print Lilei.age
print Lilei.name

Lilei.color('black')            #调用类中的方法
