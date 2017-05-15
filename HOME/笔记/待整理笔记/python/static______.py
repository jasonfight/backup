#!/usr/bin/python
#coding=utf-8
'''
这个是类方法还是静态方法?二者如何区别?

执行结果:
10
10
Man
lilei is Black
Hanmei is yellow
'''
class Person(object):
    ''' This is a class'''
    age = 10
    name = 'lilei'

    def color(self,color):
        self.language = 'english'
        print '%s is %s'%(self.name,color)

Lilei = Person()
Hanmei =  Person()
Lilei.sex = 'Man'
Hanmei.name = "Hanmei"

print Lilei.age
print Person.age
print Lilei.sex
Lilei.color('Black')
Hanmei.color('yellow')
