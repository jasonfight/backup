#!/usr/bin/python
#coding=utf-8

'''
还没搞清楚super函数到底怎么用!!!!!
super函数的使用:
super(子类名称,self).__init__()

父类 Bird1 中的 __init__  中只有hungry 属性
父类 Bird2 中的__init__ 中 只有 call 属性
子类 SongBird 中 也使用了__init__ 但没有定义任何属性,
当子类 SongBird 想使用 

'''

class Bird1(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print "Aaaaah"
            self.hungry=False
        else:
            print 'No Thanks'

class Bird2(object):
    def __init__(self):
        self.call='gugugugu'
    def talk(self):
        print self.call

class SongBird(Bird1,Bird2):
    def __init__(self):
       super(SongBird,self).__init__()
	
    def eat(self):
        print 'songbird eat'
    def talk(self):
        print 'songbird talk'

niao = SongBird()
niao.eat()
niao.talk()
print "-----------"
super(SongBird,niao).eat()

#SongBird.eat()
#super(SongBird,niao).talk()	#只能是用super继承一个父类的属性





