#!/usr/bin/python
#coding=utf-8

'''
私有化
代码有问题!!!!!!!需要更正

'''
class Student(object):
    def __init__(self):
    	pass

    def getScore(self):
        return self.__score

    def setScore(self,value):
        if value < 0 or value > 100:
            raise ValueError('score must between 1--100')
        self.__score = value


s=Student()

s.setScore(101)

print s.getScore()
