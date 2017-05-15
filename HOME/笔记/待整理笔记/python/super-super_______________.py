#!/usr/bin/python
#coding=utf-8
'''
super函数的使用:
执行结果:
Diaochan is a girl,she is about160,and her weight is 90
Diaochan is about 160
==============
xishi is about 160
'''

class Person(object):
    def __init__(self):
        self.height=160

    def about(self,name):
        print ('{} is about {}'.format(name,self.height))

class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()
        self.weight = 90

    def about(self,name):
        print('{} is a girl,she is about{},and her weight is {}').format(name,self.height,self.weight)
        super(Girl,self).about(name)

chan=Girl()
shi=Girl()

chan.about('Diaochan')
print '=============='
super(Girl,shi).about('xishi')
