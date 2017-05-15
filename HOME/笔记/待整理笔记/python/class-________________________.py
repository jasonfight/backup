#!/usr/bin/python
#coding=utf-8
'''
类的创建,类的实例化及使用

输出结果:
38
38
Bryant is black,he's num is 24
his city is los angeles
gasol is white,he's num is 16
his city is los angeles

'''
class Player(object):
    age = 38
    team = "Lakers"
    coach = "Philip jackson"
    def __init__(self,name):
        self.name = name

    def inf(self,color):
        self.city = 'los angeles'
        print "%s is %s,he's num is %d"%(self.name,color,self.num)

kobe = Player("Bryant")
paul = Player("gasol")
kobe.num = 24
paul.num = 16
print kobe.age
print paul.age
kobe.inf('black')
print "his city is",kobe.city
paul.inf('white')
print "his city is",paul.city
