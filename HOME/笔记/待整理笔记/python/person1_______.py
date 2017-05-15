#!/usr/bin/python

class Person(object):
    
    print("class....")
    def __new__(cls):
        print('new.......')
        return object.__new__(cls)

    def __init__(self):
        print("init......")

    def __del__(self):
        print("del....")

    def getName(self):
        return self.name

    def color(self,color):
        print("%s is %s"%(self.name,color))

Lilei = Person()

Lilei.name = 'lilei'

print(Lilei.getName())
Lilei.color('black')

