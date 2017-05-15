#!/usr/bin/python

class Animal(object):

    print "A new animal!!"

    def call(self,yell):
        self.yell = yell

class Dog(Animal):
    color = "yellow"

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

class Cat(Animal):
    color = "white"
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name                # NOTE:  setName 和 getName的作用??????

if __name__ == '__main__':           # NOTE: 测试用,当直接运行模块时,__name__为__main__,当被调用时,__name__为模块名
    wang = Dog()
    miao = Cat()

    wang.setName("dahuang")
    miao.setName("xiaomiao")

    print wang.getName()
    print miao.getName()

    wang.call("wangwang")
    print wang.yell
    miao.call("miaomiao")
    print miao.yell
